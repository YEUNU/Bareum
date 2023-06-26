from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Review
from .serializers import ReviewSerializer

# Create your views here.

class ReviewList(APIView):
    
    def get(self, request):
        nutraceuticals_name = request.GET.get('nutraceuticals_name', None)
        if nutraceuticals_name:
            reviews = Review.objects.filter(nutraceuticals_name=nutraceuticals_name)
        else:
            reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)