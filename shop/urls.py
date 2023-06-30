from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cart/',views.CartView.as_view()),
    path('payment/',views.paymentView.as_view()),
    
    
]
