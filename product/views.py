from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from rest_framework.views import APIView
from .models import Nutraceuticals
from rest_framework.response import Response
from .serializers import NutraSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Review
from .serializers import ReviewSerializer

# Create your views here.

class ProductDetailView(APIView):
    serializer = NutraSerializer 
    def get(self,request,product_code):
        try:
            product = Nutraceuticals.objects.get(pk=product_code)
        except Nutraceuticals.DoesNotExist:
            
            return JsonResponse({"message": "Product not found"}, status=404)
        serializer = self.serializer(product)
        return Response(data= serializer.data, status=status.HTTP_200_OK)        
        
class ReviewList(APIView):
    
    def get(self, request,product_code):
        try:
            reviews = Review.objects.filter(제품코드=product_code)
        except Review.DoesNotExist:
            return JsonResponse({"message": "review not found"}, status=404)

        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request,product_code):
        serializer = ReviewSerializer(제품코드=product_code)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


