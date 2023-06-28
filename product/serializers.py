from rest_framework import serializers
from .models import Nutraceuticals,Review
# serializers.py
from rest_framework import serializers
from .models import Review, BareumReview,BareumReviewImage
from account.models import User, ProfileImage
from account.serializer import ProfileSerializer
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        
class NutraSerializer(serializers.ModelSerializer):
    Review = ReviewSerializer
    class Meta:
        model = Nutraceuticals
        fields = '__all__'

class BareumReviewImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BareumReviewImage
        fields = ('review_img_url',)


class BareumReviewSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()  # 새로운 필드를 추가하세요.
    user_info = serializers.SerializerMethodField()  # 새로운 필드 user_info를 추가하세요.
    class Meta:
        model = BareumReview
        fields = '__all__'

    def get_images(self, obj):
        images = BareumReviewImage.objects.filter(review=obj)

        if images:
            img_serializer = BareumReviewImageSerializer(images, many=True)
            return img_serializer.data
        else:
            return []
        
    def get_user_info(self, obj):
        user = obj.writer
        user_serializer = BareumUserSerializer(user)
        return user_serializer.data   
    
    
class BareumUserSerializer(serializers.ModelSerializer):
    profile_image = serializers.SerializerMethodField() 
    class Meta:
        model = User
        fields = ('nickname','profile_image')
        
    def get_profile_image(self, obj):
        return ProfileSerializer.get_profile_image_url(obj)
    

class TotalRankingReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('제품코드_id','lowest','average_rating','total_reviews')
class TotalRankingBareumReviewSeiralizer(serializers.ModelSerializer):
    class Meta:
        model = BareumReview
        fields = ('제품코드_id','rating')
        
class TotalRankingSerializer(serializers.ModelSerializer):
    review = serializers.SerializerMethodField()
    bareum_review = serializers.SerializerMethodField()

    class Meta:
        model = Nutraceuticals
        fields = ('업체별_제품코드','review','bareum_review','업소명','nutraceuticals_name','bareum_certification')

    def get_review(self, obj):
        try:
            review = Review.objects.get(제품코드_id=obj.업체별_제품코드)
            return TotalRankingReviewSerializer(review).data
        except Review.DoesNotExist:
            return {'제품코드_id' : obj.업체별_제품코드,
                    'lowest':'---',
                    'average_rating':0,
                    'total_reviews':0}

    def get_bareum_review(self, obj):
        total_rating = 0
        number_of_ratings = BareumReview.objects.filter(제품코드_id=obj.업체별_제품코드).count()

        if number_of_ratings == 0:
            return {
            'average_rating': 0,
            'total_reviews': 0
        }

        for review in BareumReview.objects.filter(제품코드_id=obj.업체별_제품코드):
            total_rating += review.rating

        average_rating = total_rating / number_of_ratings

        return {
            'average_rating': average_rating,
            'total_reviews': number_of_ratings
        }