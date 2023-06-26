from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from . import views

urlpatterns = [
    path('login',views.login_user),
    path('signup',views.signup),
    path('logout',views.logout_user),
    path('login/signup', lambda request: redirect('login')),
    path('kakao/login',views.KakaoLogin.as_view()),
    path('check_session/',views.check_session),
    path('session/',views.session),
    path('profile/img/<int:member_id>',views.UserProfileImageView.as_view()),
    path('addInfo/<int:member_id>/',views.UserAddInfoView.as_view()),
    path("address/<int:member_id>/", views.UserAddressView.as_view(), name="user_address"),
    path('address/remove/<int:member_id>',views.user_remove),
    
]
