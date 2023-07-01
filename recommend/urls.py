from django.urls import path
from . import views

urlpatterns = [
    path('', views.pr_recommend),
    path('age/',views.AgeRecommendView.as_view()),
    path('interest/',views.InterestRecommendView.as_view()),
]