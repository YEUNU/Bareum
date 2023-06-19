from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('list/', views.PostListView.as_view(), name='post-list'),
    path('write',views.write_post),
    path('detail/<int:post_id>/',views.post_detail)
    path('popularlist/', views.popular_posts, name='popular_posts'),
]
