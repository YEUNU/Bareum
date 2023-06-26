from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('detail/<str:product_code>/', views.ProductDetailView.as_view()),
    path('reviews/<str:product_code>/', views.ReviewList.as_view(), name='review-list'),
]
