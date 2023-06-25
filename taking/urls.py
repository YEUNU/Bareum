from django.urls import path
from . import views
from .views import NutraceuticalsSearchAPIView, NutraceuticalsSaveAPIView

app_name = 'api'

urlpatterns = [
    path('search', NutraceuticalsSearchAPIView.as_view()),
    path('save', NutraceuticalsSaveAPIView.as_view()),  # 메서드 지정
]
