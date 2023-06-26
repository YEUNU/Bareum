from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from product.models import Nutraceuticals
from .serializers import NutraceuticalsSerializer
from product.models import eating_Nutraceuticals

class NutraceuticalsSearchAPIView(generics.ListAPIView):
    queryset = Nutraceuticals.objects.all()
    serializer_class = NutraceuticalsSerializer

    def get_queryset(self):
        search_query = self.request.query_params.get("search_query")
        print(search_query)
        return self.queryset.filter(nutraceuticals_name__icontains=search_query)

# 새로운 view 추가
class NutraceuticalsSaveAPIView(generics.GenericAPIView):
    queryset = Nutraceuticals.objects.all()
    serializer_class = NutraceuticalsSerializer
    
    def post(self, request):
        for item in request.data['checkedItems']:
            eating = eating_Nutraceuticals(
                nutraceuticals_name = item['nutraceuticals_name'],
                login_id = item['loginId']
            )
            eating.save()
        return Response({"message": "success"})
            


        
            