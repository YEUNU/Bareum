from PIL import Image
from django.core.files.storage import default_storage
from django.http import JsonResponse
from .modules.modules_ocr import ocr
import numpy as np

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

 

    return JsonResponse({"error": "Invalid request"})