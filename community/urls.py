from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('list/', views.PostListView.as_view(), name='post-list'),
    path('write',views.write_post),
    path('detail/<int:post_id>/',views.post_detail),
    path('popularlist/', views.popular_posts, name='popular_posts'),
    path('comments/<int:post_id>', views.CommentListView.as_view(), name='comments_list'),
    path('comments/reply/<int:comments_id>',views.CommentReplyListView.as_view(), name='comments_reply_list')
]
