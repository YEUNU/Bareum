from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from rest_framework.views import APIView
from .models import Nutraceuticals
from rest_framework.response import Response
from .serializers import NutraSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Review, BareumReview
from .serializers import ReviewSerializer, BareumReviewSerializer

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
            reviews = Review.objects.get(제품코드=product_code)
        except Review.DoesNotExist:
            return JsonResponse({"message": "review not found"}, status=404)

        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    


class BareumReviewList(APIView):
    
    def get(self,request,product_code):
        try:
            reviews = BareumReview.objects.filter(제품코드=product_code)
        except BareumReview.DoesNotExist:
            return JsonResponse({"message": "review not found"}, status=404)
        
        serializer = BareumReviewSerializer(reviews, many=True)
        return Response(serializer.data)
        