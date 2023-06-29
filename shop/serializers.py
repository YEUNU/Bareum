from rest_framework import serializers
from .models import Order,OrderItem,ShoppingCart
from product.models import Nutraceuticals,Review

class NutraceuticalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutraceuticals
        fields = ('업소명','nutraceuticals_name','업체별_제품코드')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ()

class CartSerializer(serializers.ModelSerializer):
    product = NutraceuticalsSerializer()
    lowest = serializers.SerializerMethodField()

    class Meta:
        model = ShoppingCart
        fields = '__all__'

    def get_lowest(self, obj):
        try:
            review = Review.objects.get(제품코드_id=obj.product.업체별_제품코드)
            return review.lowest
        except Review.DoesNotExist:
            return None
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
