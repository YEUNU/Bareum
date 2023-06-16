from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from models import Post

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