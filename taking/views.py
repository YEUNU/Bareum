from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from product.models import Nutraceuticals
from .serializers import NutraceuticalsSerializer
from .models import eating_Nutraceuticals
from django.core.exceptions import ObjectDoesNotExist

class NutraceuticalsSearchAPIView(generics.ListAPIView):
    queryset = Nutraceuticals.objects.all()
    serializer_class = NutraceuticalsSerializer

    def get_queryset(self):
        search_query = self.request.query_params.get("search_query")
        print(search_query)
        return self.queryset.filter(nutraceuticals_name__icontains=search_query)

# 새로운 view 추가
from django.core.exceptions import ObjectDoesNotExist

class NutraceuticalsSaveAPIView(generics.GenericAPIView):
    queryset = Nutraceuticals.objects.all()
    serializer_class = NutraceuticalsSerializer
    
    def post(self, request):
        all_successful = True

        for item in request.data['checkedItems']:
            try:
                # 이미 존재하는지 확인
                existing_item = eating_Nutraceuticals.objects.get(
                    nutraceuticals_name=item['nutraceuticals_name'],
                    login_id=item['loginId']
                )
                all_successful = False
            except ObjectDoesNotExist:
                # 기존 항목이 없으면 새 항목을 저장함
                eating = eating_Nutraceuticals(
                    nutraceuticals_name=item['nutraceuticals_name'],
                    login_id=item['loginId']
                )
                eating.save()

        if all_successful:
            return Response({"message": "success"})
        else:
            return Response({"message": "fail"})

            


        
            