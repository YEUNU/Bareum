from django.urls import path
from . import views
from .views import NutraceuticalsSearchAPIView, NutraceuticalsSaveAPIView

app_name = 'api'

urlpatterns = [
    path('', views.get_user_nutrients_data),
    path('search', NutraceuticalsSearchAPIView.as_view()),
    path('save', NutraceuticalsSaveAPIView.as_view()),
    path('regist', views.view_take),
    path('remove', views.RemoveNutraceuticalView.as_view()),
]
