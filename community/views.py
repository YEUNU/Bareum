from django.shortcuts import render
from .models import Post
from rest_framework import generics
from .serializers import PostSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers, status
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import date
from .models import User
import django.core.serializers as dserializers 
from django.db.models import Count
from rest_framework.decorators import api_view
# Create your views here.



# 게시물을 표시하는 데 사용되는 직렬화 클래스
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post      # 게시물 모델 클래스
        fields = '__all__'

# 페이지 번호로 게시물을 반환하는 paginator 클래스
class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    max_page_size = 1000

class PostListView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Post.objects.all().order_by('-post_date')  # 레코드를 명시적으로 정렬
        paginator = CustomPageNumberPagination()
        paginated_posts = paginator.paginate_queryset(queryset, request)
        serializer = PostSerializer(paginated_posts, many=True)
        return paginator.get_paginated_response(serializer.data)





# api/community/newslist?page=${pageNumber}   영양뉴스를 페이징해서 가져옴
# api/community/list?page=${pageNumber}  게시물을 페이징 해서 가져옴
# api/community/detail?id=${this.postId}  게시글 가져오기  user id 랑 name 도 넘겨줄것
# api/community/popularlist
# api/community/write


#글쓰기
@csrf_exempt   
def write_post(req):
    if req.method == 'POST':
        data = json.loads(req.body)
        print(data)
        title = data.get('title')
        contents = data.get('content')
        id = data.get('memberId')
        print(title, contents,id)
        user = User.objects.get(member_id = id)
        post = Post.objects.create(post_title=title, post_contents=contents,
                                   post_date = date.today(), post_like = 0, post_category = 'normal', user=user)
        
        response_data = {'post_title':post.post_title, 'post_contents':post.post_contents}
        
        return JsonResponse(response_data, status=201)
  
#게시글 제목 검색 
def search_posts(request):
    search_query = request.GET.get('searchQuery', '')
    print(f"Search query: {search_query}")
    
    filtered_posts = Post.objects.filter(post_title__icontains=search_query)
    serialized_posts = dserializers.serialize('json', filtered_posts)
    return JsonResponse(serialized_posts, safe=False)


#인기글 보여주기(좋아요0개임)
@api_view(['GET'])
def popular_posts(request):
    popular_posts = Post.objects.filter(post_like__gte=0).annotate(num_likes=Count('post_like')).order_by('-num_likes', '-post_date')
    serialized_posts = dserializers.serialize('json', popular_posts)
    return JsonResponse({"data": serialized_posts}, safe=False)
        

    
    
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder

def post_detail(request, post_id):
    try:
        post = Post.objects.select_related('user').get(post_id=post_id)
    except Post.DoesNotExist:
        return JsonResponse({"message": "Post not found"}, status=404)

    post_data = {
        "post_id": post.post_id,
        "post_date": post.post_date,
        "post_title": post.post_title,
        "post_contents": post.post_contents,
        "post_like": post.post_like,
        "post_category": post.post_category,
        "user_id": post.user.member_id,
        #나중에 닉네임으로 수정해야할듯
        "user_name": post.user.user_name,
    }

    return JsonResponse(post_data, encoder=DjangoJSONEncoder)