from django.http import JsonResponse
import pandas as pd
import os 
from taking.models import eating_Nutraceuticals
from product.models import Nutraceuticals
from django.views.decorators.csrf import csrf_exempt
import json 

def find_best_supplement(all_df, need_nut, already_selected, max_intake_limits_df):
    min_difference = float('inf')
    best_supplement = None
    best_index = None

    for idx, row in all_df.iterrows():
        if idx in already_selected:
            continue

        row_difference = 0
        for nutrient in need_nut.columns:

            allowed_intake = min(max_intake_limits_df.loc[0, nutrient], need_nut.loc[0, nutrient])
            row_difference += max(need_nut.loc[0, nutrient] - min(row[nutrient], allowed_intake), 0)

        if row_difference < min_difference:
            min_difference = row_difference
            best_supplement = row
            best_index = idx

    return best_index, best_supplement

@csrf_exempt
def pr_recommend(req):
    if req.method == "POST":
        data = json.loads(req.body)
        user_id = data['loginId']
        user_nutraceuticals = eating_Nutraceuticals.objects.filter(login_id=user_id)
        nut_name = [n.nutraceuticals_name for n in user_nutraceuticals]
        print('login_id : ' + user_id)
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
        
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        csv_dir = os.path.join(cur_dir, 'total_nutrition.csv')
        all_df = pd.read_csv(csv_dir)
        
        user_input = {
            "비타민C" : [0],
            "비타민D" : [0],
            "비타민A" : [0],
            "칼슘" : [0],
            "마그네슘" : [0],
            "아연" : [0],
        }
        for i in response_data:
            for j in i:
                user_input[j][0] += i[j]
        print(user_input)
        user_input_df = pd.DataFrame(user_input)
        print(user_input_df)
        recommend_official = {
            "비타민C" : [100],
            "비타민D" : [10],
            "비타민A" : [700],
            "칼슘" : [700],
            "마그네슘" : [315],
            "아연" : [8.5],
        }
        recommend_official_df = pd.DataFrame(recommend_official)

        max_intake_limits = {
            "비타민C": [2000],
            "비타민D": [4000],
            "비타민A": [3000],
            "칼슘": [2500],
            "마그네슘": [350],
            "아연": [35],
        }
        max_intake_limits_df = pd.DataFrame(max_intake_limits)
        
        already_selected = []
        current_demand = (recommend_official_df - user_input_df) / recommend_official_df

        while current_demand.mean(axis=1)[0] > 0:
            best_index, best_supplement = find_best_supplement(all_df, current_demand, already_selected, max_intake_limits_df)
            user_input_df.loc[0] += best_supplement
            already_selected.append(best_index)

            current_demand = (recommend_official_df - user_input_df) / recommend_official_df


        # 결과 출력
        result = ['츄어블비타민C', '고려홍삼차']
        for idx in already_selected:
            result.append(all_df.loc[idx, 'name'])
        print(result)
        
        response_data = []
        for name in result:
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