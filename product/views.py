from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from rest_framework.views import APIView
from .models import Nutraceuticals
from rest_framework.response import Response
from .serializers import NutraSerializer
from rest_framework import serializers, status

# Create your views here.

class ProductDetailView(APIView):
    serializer = NutraSerializer 
    def get(self,request,product_code):
        try:
            product = Nutraceuticals.objects.get(pk=product_code)
        except Nutraceuticals.DoesNotExist:
            
            return JsonResponse({"message": "Post not found"}, status=404)
        serializer = self.serializer(product)
        print(serializer.data)
        return Response(data= serializer.data, status=status.HTTP_200_OK)        
    


