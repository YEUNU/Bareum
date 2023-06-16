from django.shortcuts import render
from .models import Post
from rest_framework import generics
from .serializers import PostSerializer
from django.http import HttpResponse, JsonResponse

# Create your views here.
class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
# def return_post(req):
#     if req.method == 'GET':
#         post_id = Post.post_id
#         post_title = Post.post_title
#         post_contents = Post.post_contents
#         post_like = Post.post_like
#         post_category = Post.post_category
#         return JsonResponse({'post_id':post_id,'post_title':post_title,'post_contents':post_contents,
#                              'post_like':post_like, 'post_category':post_category})

#     else:
#         return JsonResponse({'error': '잘못된 요청입니다.'}, status=400)