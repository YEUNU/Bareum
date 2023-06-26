from rest_framework import serializers
from .models import Nutraceuticals,Review
# serializers.py
from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        
class NutraSerializer(serializers.ModelSerializer):
    Review = ReviewSerializer
    class Meta:
        model = Nutraceuticals
        fields = '__all__'

    

        fields = '__all__'
