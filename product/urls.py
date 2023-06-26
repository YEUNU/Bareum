from django.contrib import admin
from django.urls import path, include
from . import views
from .views import ReviewList

urlpatterns = [
    path('detail/<int:nutra_id>/',views.ProductDetailView.as_view()),
    
    
    path('reviews/', ReviewList.as_view(), name='review-list'),
]
