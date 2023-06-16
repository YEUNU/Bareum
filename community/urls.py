from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PostListAPIView.as_view())
    # path('', views.return_post)
]
