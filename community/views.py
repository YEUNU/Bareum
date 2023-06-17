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
        queryset = Post.objects.all()
        paginator = CustomPageNumberPagination()
        paginated_posts = paginator.paginate_queryset(queryset, request)
        serializer = PostSerializer(paginated_posts, many=True)
        return paginator.get_paginated_response(serializer.data)





# api/community/newslist?page=${pageNumber}   영양뉴스를 페이징해서 가져옴
# api/community/list?page=${pageNumber}  게시물을 페이징 해서 가져옴
# api/community/detail?id=${this.postId}  게시글 가져오기  user id 랑 name 도 넘겨줄것
# api/community/popularlist
# api/community/write



@csrf_exempt   
def write_post(req):
    if req.method == 'POST':
        data = json.loads(req.body)
        print(data)
        title = data.get('title')
        contents = data.get('content')
        id = data.get('memberId')
        print(title, contents,id)
        post = Post.objects.create(post_title=title, post_contents=contents,
                                   post_date = date.today(), post_like = 0, post_category = 'normal', user=id)
        
        response_data = {'post_title':post.post_title, 'post_contents':post.post_contents}
        
        return JsonResponse(response_data, status=201)
    