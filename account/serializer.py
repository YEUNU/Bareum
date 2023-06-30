from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import ProfileImage, Address, UserInterest
# class UserSerializer (serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = [ 'url', 'username' , 'email', 'groups' ]

# class GroupSerializer (serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = [ 'url', 'name']
        
# class PostSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model= Post
#         fields=['title','content']
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_name','member_id']
        
class ProfileSerializer(serializers.ModelSerializer):
    profile_image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = ProfileImage
        fields = '__all__'

    @staticmethod
    def get_profile_image_url(user):
        no_image_url = '/media/profile_images/default_profile_image.png'
        profile_image_url = no_image_url  # 기본값으로 no-image.jpg 경로를 지정합니다.

        try:
            # 해당 유저의 프로필 이미지가 존재하면 해당 이미지 경로를 반환합니다.
            profile_image = ProfileImage.objects.get(user=user)
            profile_image_url = profile_image.image.url
        except ProfileImage.DoesNotExist:
            pass

        return profile_image_url

class UserAddInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= ['nickname','birthday','height','weight','gender']
    


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
        
        
class InterestSerializer(serializers.Serializer):
    interest = serializers.ListField()

    def create(self, validated_data):
        return UserInterest.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass