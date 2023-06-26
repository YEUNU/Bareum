from django.contrib import admin
from django.urls import path, include
from . import views
from .views import ReviewList

urlpatterns = [
    path('detail/<str:product_code>/', views.ProductDetailView.as_view()),

    
    
    path('reviews/', ReviewList.as_view(), name='review-list'),
]
