# views.py
from django.shortcuts import render
from rest_framework import generics
from product.models import Nutraceuticals
from .serializers import NutraceuticalsSerializer

class NutraceuticalsSearchAPIView(generics.ListAPIView):
    queryset = Nutraceuticals.objects.all()
    serializer_class = NutraceuticalsSerializer

    def get_queryset(self):
        search_query = self.request.query_params.get("search_query")
        print(search_query)
        return self.queryset.filter(nutraceuticals_name__icontains=search_query)
