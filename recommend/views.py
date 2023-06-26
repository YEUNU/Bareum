from django.http import JsonResponse
import numpy as np
import pandas as pd
from collections import defaultdict
import difflib
import os 
from product.models import eating_Nutraceuticals, Ingredient

from django.views.decorators.csrf import csrf_exempt
import json 

@csrf_exempt
def pr_recommend(req):
    if req.method == "POST":
        data = json.loads(req.body)
        user_id = data['loginId']
        user_nutraceuticals = eating_Nutraceuticals.objects.filter(login_id=user_id)
        nut_name = [n.nutraceuticals_name for n in user_nutraceuticals]
        
        response_data = []
        for name in nut_name:
            ingredient = Ingredient.objects.get(nutraceuticals_name=name)
            response_data.append({
                "name" : ingredient.nutraceuticals_name,
                '비타민C': ingredient.비타민C,
                '비타민D': ingredient.비타민D,
                '비타민A': ingredient.비타민A,
                '칼슘': ingredient.칼슘,
                '마그네슘': ingredient.마그네슘,
                '아연': ingredient.아연,
            })
        print(response_data)
        
        return JsonResponse(response_data, safe=False)