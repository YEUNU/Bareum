from django.urls import path
from . import views
from .views import NutraceuticalsSearchAPIView
app_name = 'api'

urlpatterns = [
    path('search',NutraceuticalsSearchAPIView.as_view()),
]