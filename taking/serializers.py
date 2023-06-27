from rest_framework import serializers
from product.models import Nutraceuticals
from . models import eating_Nutraceuticals
class NutraceuticalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutraceuticals
        fields = '__all__'
        
class eating_NutraceuticalSerializer(serializers.ModelSerializer):
    class Meta:
        model = eating_Nutraceuticals
        fields = '__all__'