from rest_framework import serializers
from product.models import Nutraceuticals

class NutraceuticalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutraceuticals
        fields = '__all__'