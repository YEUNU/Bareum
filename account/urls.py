from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from . import views

urlpatterns = [
    path('login',views.login_user),
    path('signup',views.signup),
    path('login/signup', lambda request: redirect('login')),
    path('kakao/login',views.KakaoLogin.as_view())
]
