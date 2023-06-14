from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login',views.login),
    path('signup',views.signup),
    path('login-kakao',views.login_kakao)
]
