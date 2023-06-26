from django.contrib import admin
from django.urls import path, include
from . import views
from .views import ReviewList

urlpatterns = [
    path('reviews/', ReviewList.as_view(), name='review-list'),
]
