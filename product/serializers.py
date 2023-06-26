from rest_framework import serializers
from .models import Nutraceuticals,Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        
class NutraSerializer(serializers.ModelSerializer):
    Review = ReviewSerializer
    class Meta:
        model = Nutraceuticals
        fields = '__all__'

    

