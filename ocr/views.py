from PIL import Image
from django.core.files.storage import default_storage
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .modules.modules_ocr import ocr

@csrf_exempt
def process_image(request):
    if request.method == "POST" and request.FILES["image"]:
        image = request.FILES["image"]

        image_path = default_storage.save("temp.jpg", image)
        img = Image.open(image_path)
        img.save('./ocr/temp/temp_ocr.png')
        
        model = ocr()
        
        result_ocr = model("./ocr/temp/temp_ocr.png")
        print(result_ocr)

    return JsonResponse({"error": "Invalid request"})
