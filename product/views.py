from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from rest_framework.views import APIView
from .models import Nutraceuticals
from rest_framework.response import Response
from .serializers import NutraSerializer
from rest_framework.response import Response
from rest_framework import status
from account.models import User
from .models import Review, BareumReview,BareumReviewImage
from .serializers import ReviewSerializer, BareumReviewSerializer
from django.core.files.storage import default_storage

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
            reviews = Review.objects.filter(제품코드_id=product_code)
        except Review.DoesNotExist:
            return JsonResponse({"message": "review not found"}, status=404)

        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BareumReviewList(APIView):
    def get(self,request,product_code):
        try:
            reviews = BareumReview.objects.filter(제품코드_id=product_code)
        except BareumReview.DoesNotExist:
            return JsonResponse({"message": "review not found"}, status=404)
        serializer = BareumReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self,request,product_code):
        reviews = request.POST['reviews']
        rating = request.POST['rating']

        try:
            nutra = Nutraceuticals.objects.get(업체별_제품코드=product_code)
            review = BareumReview.objects.create(
                제품코드_id = nutra.업체별_제품코드,
                nutraceuticals_name = nutra.nutraceuticals_name,
                company_name = nutra.업소명,
                reviews = reviews,
                rating = rating,
                writer = request.user,            
            )

            if len(request.FILES) > 0:
                for key in request.FILES:
                    image_file = request.FILES[key]
                    image = BareumReviewImage()
                    image.review_img_url = default_storage.save(
                        "review_images/%s" % (image_file.name,),
                        image_file
                    )
                    image.review = review
                    image.save()
                    
        except Nutraceuticals.DoesNotExist:
            return Response({"error": "제품이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(str(e))
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response({}, status=status.HTTP_201_CREATED)
    

        
class MyReviewList(APIView):
    def get(self,request,member_id):
        try:
            reviews = BareumReview.objects.filter(writer=member_id)
        except BareumReview.DoesNotExist:
            return JsonResponse({"message": "review not found"}, status=404)
        serializer = BareumReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class TotalRankingList(APIView):
    def get(self, request):
        try:
            top_nutra = Nutraceuticals.objects.order_by('-score')[:10]
            serializer = NutraSerializer(top_nutra, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)