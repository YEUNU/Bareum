from django.http import JsonResponse
import pandas as pd
import numpy as np
import os 
from taking.models import eating_Nutraceuticals
from product.models import Nutraceuticals
from account.models import User
from sklearn.metrics.pairwise import cosine_similarity
from django.views.decorators.csrf import csrf_exempt
from collections import deque
import json 
import datetime
import pickle
from django.db.models import F, Q
from product.serializers import TotalRankingSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

@csrf_exempt
def pr_recommend(req):
    if req.method == "POST":
        data = json.loads(req.body)
        user_id = data['loginId']
        user_nutraceuticals = eating_Nutraceuticals.objects.filter(login_id=user_id)
        nut_name = [n.nutraceuticals_name for n in user_nutraceuticals]
        user = User.objects.get(login_id=user_id)
        gender = user.gender
        age = datetime.date.today().year - user.birthday.year
        if gender == 'male':
            gender = 1
        else:
            gender = 0
        
        response_data = []
        for name in nut_name:
            ingredient = Nutraceuticals.objects.get(nutraceuticals_name=name)
            response_data.append({
                '비타민C': ingredient.비타민C,
                '비타민D': ingredient.비타민D,
                '비타민A': ingredient.비타민A,
                '칼슘': ingredient.칼슘,
                '마그네슘': ingredient.마그네슘,
                '아연': ingredient.아연,
            })
        
        data = {"age" : age,"비타민C": 0, "비타민D": 0, 
                "비타민A": 0, "칼슘": 0, "마그네슘" : 0, "아연" : 0,
                "sex_male" : gender}
        
        for i in response_data:
            for j in i:
                data[j] += i[j]
        user_input_df = pd.DataFrame(data, index=[0])
        user_input_df = pd.get_dummies(user_input_df)
        
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        csv_dir = os.path.join(cur_dir, 'total_nutrition.csv')
        all_df = pd.read_csv(csv_dir)
   
        current_path = os.path.dirname(os.path.abspath(__file__))
        pkl_file = os.path.join(current_path, "best_model_xgb.pkl")
        xgb_reg = pickle.load(open(pkl_file, "rb"))
        user_nut = xgb_reg.predict(user_input_df)
        lowest = 0.0
        recommend_item = deque()
        user_nut2 = [[0,0,0,0,0,0]]
        user_nut2[0][0] = user_nut[0][2]
        user_nut2[0][1] = user_nut[0][3]
        user_nut2[0][2] = user_nut[0][1]
        user_nut2[0][3] = user_nut[0][5]
        user_nut2[0][4] = user_nut[0][0]
        user_nut2[0][5] = user_nut[0][4]
        for i in range(len(user_nut2[0])):
            if user_nut2[0][i] <= 0.0:
                user_nut2[0][i] = 0
        # after_nut = list()
        # before_nut = user_input_df.copy()
        maxValues = [100, 20, 700, 700, 315, 8.5]
        for i in range(len(user_nut2[0])):
            user_nut2[0][i] = (user_nut2[0][i] / maxValues[i]) * 100
        
        cos_list = []
        for i in all_df.iterrows():
            temp = i[1][["비타민C","비타민D","비타민A","칼슘","마그네슘","아연"]]
            x = [temp.values]
            for j in range(6):
                x[0][j] = (x[0][j] / maxValues[j]) * 100
            cos_list.append((abs(cosine_similarity(user_nut2, x))[0][0], all_df["name"][i[0]]))

        new_recommend_item = []
        for i in range(5):
            new_recommend_item.append(sorted(cos_list, reverse=True)[i][1])
        response_data = []
        for name in new_recommend_item:
            pr = Nutraceuticals.objects.get(nutraceuticals_name=name)
            response_data.append({
                '제품코드' : pr.업체별_제품코드,
                '제품명': pr.nutraceuticals_name,
                '업소명': pr.업소명,
                '광고상품' : pr.ad,
            })
        response_data = sorted(response_data, key=lambda x: x['광고상품'], reverse=True)
        return JsonResponse({"nutraceuticals": response_data}, safe=False)
    
class AgeRecommendView(APIView):
    def get(self, request):
        try:
            ingredients = request.GET.get('ingredients')
            ingredients_list = json.loads(ingredients)
            queryset = Nutraceuticals.objects.none()

            for ingredient in ingredients_list:
                column_condition = Q(**{ingredient + '__gt': 0})
                queryset |= Nutraceuticals.objects.filter(column_condition)

            top_nutra = queryset.order_by('-score')[:3]
            serializer = TotalRankingSerializer(top_nutra, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    

class InterestRecommendView(APIView):
    def get(self,request):
        print('엥?')
        try:
            ingredients = request.GET.get('ingredients')
            ingredients_list = json.loads(ingredients)
            print("asd: ",ingredients_list)
            queryset = Nutraceuticals.objects.none()

            for ingredient in ingredients_list:
                column_condition = Q(**{ingredient + '__gt': 0})
                queryset |= Nutraceuticals.objects.filter(column_condition)

            top_nutra = queryset.order_by('-score')[:3]
            serializer = TotalRankingSerializer(top_nutra, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(str(e),status= status.HTTP_400_BAD_REQUEST)