from PIL import Image
from django.http import JsonResponse
from .modules.modules_ocr import ocr
import numpy as np
import pandas as pd
from collections import defaultdict
import difflib
import os 
from product.models import Nutraceuticals

def process_image(request):
    if request.method == "POST" and request.FILES["image"]:
        image = request.FILES["image"]
        img = np.array(Image.open(image))
        model = ocr()
        result_ocr = model(img)
        string=""
        for i in result_ocr:
            if i[2] > 0.6:
                string += " " + i[1]
        string = string[1:]
        print(string)

        cur_dir = os.path.dirname(os.path.abspath(__file__))
        csv_dir = os.path.join(cur_dir, 'total_nutrition.csv')
        names = pd.read_csv(csv_dir)["name"].values

        input_string = string # 인풋으로 넣을 단어혹은 문장
        input_bytes = bytes(input_string, 'utf-8') # byte로 변환
        input_bytes_list = list(input_bytes) 
        res = defaultdict(float) # DB 안에있는 이름과 비교할때 편하게 하려고 dict로 구성
        for i in names:
            answer_bytes = bytes(i, 'utf-8') # dB 안에있는 이름을 byte화
            answer_bytes_list = list(answer_bytes)
            sm = difflib.SequenceMatcher(None, answer_bytes_list, input_bytes_list) # difflib의 sequencematcher로 byte끼리 유사도 비교
            similar = sm.ratio()

            res[i] = similar # res에 저장
            
        sorted_dict = sorted(res.items(), key=lambda x: x[1]) # 유사도에 따른 정렬
        sorted_dict = sorted_dict[::-1]
        print(sorted_dict[:3])
        related_pr = []
        for i in sorted_dict:
            if i[1] >= 0.3:
                related_pr.append(i[0])
        
        result = []
        for i in related_pr[:20]:
            pr_info = Nutraceuticals.objects.filter(nutraceuticals_name=i).values('nutraceuticals_name','업소명')
            result.append(list(pr_info))

        flattened_result = [item for sublist in result for item in sublist]
        print(flattened_result)
        if len(flattened_result) == 0:
            return JsonResponse({'results':'fail'})
        
        return JsonResponse({'results': 'success', 'products':flattened_result})
    
    return JsonResponse({"error": "Invalid request"})