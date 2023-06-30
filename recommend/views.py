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

@csrf_exempt
def pr_recommend(req):
    if req.method == "POST":
        data = json.loads(req.body)
        user_id = data['loginId']
        user_nutraceuticals = eating_Nutraceuticals.objects.filter(login_id=user_id)
        nut_name = [n.nutraceuticals_name for n in user_nutraceuticals]
        print('login_id : ' + user_id)
        user = User.objects.get(login_id=user_id)
        gender = user.gender
        age = datetime.date.today().year - user.birthday.year
        if gender == 'male':
            gender = 1
        else:
            gender = 0
        print(gender, age)
        
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
        print(response_data)
        
        data = {"age" : age,"비타민C": 0, "비타민D": 0, 
                "비타민A": 0, "칼슘": 0, "마그네슘" : 0, "아연" : 0,
                "sex_male" : gender}
        
        for i in response_data:
            for j in i:
                data[j] += i[j]
        print(data)
        user_input_df = pd.DataFrame(data, index=[0])
        user_input_df = pd.get_dummies(user_input_df)
        print(user_input_df)
        
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        csv_dir = os.path.join(cur_dir, 'total_nutrition.csv')
        all_df = pd.read_csv(csv_dir)
   
        current_path = os.path.dirname(os.path.abspath(__file__))
        pkl_file = os.path.join(current_path, "best_model_xgb.pkl")
        xgb_reg = pickle.load(open(pkl_file, "rb"))
        user_nut = xgb_reg.predict(user_input_df)
        print('user_nut : ')
        print(user_nut)
        lowest = 0.0
        recommend_item = deque()
        user_nut2 = [[0,0,0,0,0,0]]
        user_nut2[0][0] = user_nut[0][2]
        user_nut2[0][1] = user_nut[0][3]
        user_nut2[0][2] = user_nut[0][1]
        user_nut2[0][3] = user_nut[0][5]
        user_nut2[0][4] = user_nut[0][0]
        user_nut2[0][5] = user_nut[0][4]
        print(user_nut2)
        for i in range(len(user_nut2[0])):
            print(user_nut2[0][i])
            if user_nut2[0][i] <= 0.0:
                user_nut2[0][i] = 0
        print(user_nut2)
        # after_nut = list()
        # before_nut = user_input_df.copy()
        maxValues = [100, 20, 700, 700, 315, 8.5]
        for i in range(len(user_nut2[0])):
            user_nut2[0][i] = (user_nut2[0][i] / maxValues[i]) * 100
        
        print(user_nut2)
        for i in all_df.iterrows():
            temp = i[1][["비타민C","비타민D","비타민A","칼슘","마그네슘","아연"]]
            x = [temp.values]
            for j in range(6):
                x[0][j] = (x[0][j] / maxValues[j]) * 100
            if abs(cosine_similarity(user_nut2, x))[0][0] > lowest:
                recommend_item.append(all_df["name"][i[0]])
                if len(recommend_item) > 5: # 5개 추천
                    recommend_item.popleft()

        print(recommend_item)
        recommend_item.append('황작 홍삼정')
        response_data = []
        for name in recommend_item:
            pr = Nutraceuticals.objects.get(nutraceuticals_name=name)
            print(pr.ad)
            response_data.append({
                '제품코드' : pr.업체별_제품코드,
                '제품명': pr.nutraceuticals_name,
                '업소명': pr.업소명,
                '광고상품' : pr.ad,
            })
        response_data = sorted(response_data, key=lambda x: x['광고상품'], reverse=True)
        print(response_data)
        return JsonResponse({"nutraceuticals": response_data}, safe=False)