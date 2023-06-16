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
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import Post

#@api_view(['GET'])
#def community_posts(request):
#    queryset = Post.objects.all()
#    paginator = PageNumberPagination()
#    paginator.page_size = 10  # 원하는 페이지 크기를 직접 지정합니다.
#
#    paginated_posts = paginator.paginate_queryset(queryset, request)
#    serializer = PostSerializer(paginated_posts, many=True)
#
#    return paginator.get_paginated_response(serializer.data)
