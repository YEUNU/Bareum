from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from product.models import Nutraceuticals
from .serializers import NutraceuticalsSerializer, eating_NutraceuticalSerializer
from .models import eating_Nutraceuticals
from django.core.exceptions import ObjectDoesNotExist
import json
from django.http import JsonResponse

class NutraceuticalsSearchAPIView(generics.ListAPIView):
    queryset = Nutraceuticals.objects.all()
    serializer_class = NutraceuticalsSerializer

    def get_queryset(self):
        search_query = self.request.query_params.get("search_query")
        login_id = self.request.query_params.get("login_id")

        user_nutraceuticals = eating_Nutraceuticals.objects.filter(login_id=login_id)

        excluded_nutraceuticals = [n.nutraceuticals_name for n in user_nutraceuticals]

        print(search_query)
        return self.queryset.filter(nutraceuticals_name__icontains=search_query).exclude(nutraceuticals_name__in=excluded_nutraceuticals)


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

        
def view_take(req):
    if req.method == "POST":
        data = json.loads(req.body)
        user_id = data['loginId']
        print('login_id : ' + user_id)
        user_nutraceuticals = eating_Nutraceuticals.objects.filter(login_id=user_id)
        nut_name = [n.nutraceuticals_name for n in user_nutraceuticals]
        response_data = []
        for name in nut_name:
            take = Nutraceuticals.objects.get(nutraceuticals_name=name)
            code = eating_Nutraceuticals.objects.get(nutraceuticals_name=name, login_id=user_id)
            response_data.append({
                '제품명': take.nutraceuticals_name,
                '업소명': take.업소명,
                'checking_number' : code.checking_number,
                '제품코드' : take.업체별_제품코드
            })
        return JsonResponse({"take": response_data}, safe=False)
    
class RemoveNutraceuticalView(generics.DestroyAPIView):
    queryset = eating_Nutraceuticals.objects.all()
    serializer_class = eating_NutraceuticalSerializer

    def delete(self, request, *args, **kwargs):
        login_id = request.data.get('loginId')
        nutraceuticals_name = request.data.get('nutraceuticals_name')

        try:
            nutraceutical_to_delete = self.queryset.get(login_id=login_id, nutraceuticals_name=nutraceuticals_name)
            nutraceutical_to_delete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except eating_Nutraceuticals.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        


def get_user_nutrients_data(request):
    user_id = request.GET.get('user_id')
    user_nutraceuticals = eating_Nutraceuticals.objects.filter(login_id=user_id).values_list('nutraceuticals_name', flat=True)
    queryset = Nutraceuticals.objects.filter(nutraceuticals_name__in=user_nutraceuticals)

    nutrients_data = []
    for nutraceutical in queryset:
        nutrients_data.append({
            '제품명' : nutraceutical.nutraceuticals_name,
            '비타민C': nutraceutical.비타민C,
            '비타민D': nutraceutical.비타민D,
            '비타민A': nutraceutical.비타민A,
            '칼슘': nutraceutical.칼슘,
            '마그네슘': nutraceutical.마그네슘,
            '아연': nutraceutical.아연,
            '제품코드' : nutraceutical.업체별_제품코드
        })
    print(nutrients_data)
    maxValues = [100, 20, 700, 700, 315, 8.5]
    nutrients_pct_data = []

    for product in nutrients_data:
        product_pct = {'제품명': product['제품명']}
        for idx, nutrient in enumerate(['비타민C', '비타민D', '비타민A', '칼슘', '마그네슘', '아연'], start=1):
            product_pct[nutrient] = product[nutrient] / maxValues[idx - 1] * 100
        nutrients_pct_data.append(product_pct)
    print(nutrients_pct_data)
    return JsonResponse(nutrients_pct_data, safe=False)



