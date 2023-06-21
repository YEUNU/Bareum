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
from datetime import datetime
from .models import User, Comments, PostImage
import django.core.serializers as dserializers 
from django.db.models import Count
from rest_framework.decorators import api_view
from django.utils import timezone
from django.core.files.storage import default_storage
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


#글쓰기
def write_post(req):
    if req.method == 'POST':
        title = req.POST['title']
        contents = req.POST['content']
        id = req.POST['memberId']
        user = User.objects.get(member_id = id)
        
        
        post = Post.objects.create(post_title=title, post_contents=contents,
                                   post_date=timezone.now(), post_like=0, post_category='normal', user=user)
        
        # 이미지 파일 저장
        for key in req.FILES:
            image_file = req.FILES[key]
            image = PostImage()
            image.image = default_storage.save("post_images/%s" % (image_file.name, ), image_file)
            image.post = post   
            image.save()

        response_data = {'post_title': post.post_title, 'post_contents': post.post_contents}
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
        "member_id": post.user.member_id,
        #나중에 닉네임으로 수정해야할듯
        "user_name": post.user.user_name,
    }

    return JsonResponse(post_data, encoder=DjangoJSONEncoder)




from .serializers import CommentsSerializer
class CommentListView(APIView):
    serializer_class = CommentsSerializer
    
    def get(self,request,post_id):
        
        try:
            comments = Comments.objects.select_related('user').filter(post_id=post_id, parent=None)
            
        except Comments.DoesNotExist:
            return JsonResponse({"message": "Post not found"}, status=404)
        


        serializer = self.serializer_class(comments, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    
    def post(self, request, post_id):
        try:
            user = User.objects.get(pk=request.data['memberId'])
            post_instance = Post.objects.get(pk=post_id)

            # request.data['user'] = user.member_id
            request.data['post'] = post_instance.post_id
            request.data['comment_date'] = timezone.now()
            request.data['comment_like'] = 0
            request.data['parent'] = None
            print(request.data)
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save(user=user, post=post_instance)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist:
            return Response({"error": "게시물이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)
        
class CommentReplyListView(APIView):
    serializer_class = CommentsSerializer
    
    def post(self, request, comments_id):
        try:
            user = User.objects.get(pk=request.data['memberId'])
            post_instance = Post.objects.get(pk=request.data['postId'])
            parent_id = comments_id

            request.data['user'] = user.member_id
            request.data['post'] = post_instance.post_id
            request.data['comment_date'] = datetime.today()
            request.data['comment_like'] = 0

            if parent_id:      # if 'parent_id' provided in request data
                parent_instance = Comments.objects.get(pk=parent_id)
                request.data['parent'] = parent_instance.comments_id
            else:
                request.data['parent'] = None   # set parent to None if there is no parent

            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save(user=user, post=post_instance)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist:
            return Response({"error": "게시물이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)
        except Comments.DoesNotExist:
            return Response({"error": "댓글이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)
        
    
    def get(self,request,comments_id):
        try:
            comment = Comments.objects.select_related('user').filter(comments_id=comments_id, parent=None)
        except Comments.DoesNotExist:
            return JsonResponse({"message": "comment not found"}, status=404)
        


        serializer = self.serializer_class(comment, many=True)
        print(serializer.data)
        return Response(data=serializer.data, status=status.HTTP_200_OK)