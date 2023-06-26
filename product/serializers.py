from rest_framework import serializers
from .models import Nutraceuticals,Review
# serializers.py
from rest_framework import serializers
from .models import Review, BareumReview

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        
class NutraSerializer(serializers.ModelSerializer):
    Review = ReviewSerializer
    class Meta:
        model = Nutraceuticals
        fields = '__all__'

    


class BareumReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = BareumReview
        fields = '__all__'