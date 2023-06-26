from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('/api/product/<int:nutra_id>/',views.ProductDetailView.as_view()),
    
    
]
