from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('detail/<str:product_code>/', views.ProductDetailView.as_view()),
    path('online-reviews/<str:product_code>/', views.ReviewList.as_view(), name='review-list'),
    path('bareum-reviews/<str:product_code>/', views.BareumReviewList.as_view(), name='bareum-review-list'),
    path('my-reviews/<int:member_id>/',views.MyReviewList.as_view(),name='my-review-list'),
    path('search/', views.search_nutraceuticals, name='search_nutraceuticals'),
    
]
