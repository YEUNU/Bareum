from django.urls import path
from . import views
urlpatterns = [
    path('result', views.process_image, name="process_image"),
]