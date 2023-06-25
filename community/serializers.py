from rest_framework import serializers
from .models import Post, Comments, User
from rest_framework_recursive.fields import RecursiveField
from account.models import ProfileImage
from account.serializer import ProfileSerializer

class UserProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileImage
        fields = ['image']
class UserSerializer(serializers.ModelSerializer):
    user_profile_img = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['user_name', 'member_id', 'nickname', 'user_profile_img']
        
    def get_user_profile_img(self, obj):
        no_image_url = '/media/profile_images/default_profile_image.png'
        profile_img = ProfileImage.objects.filter(user=obj).first()
        if profile_img:
            img_serializer = UserProfileImageSerializer(profile_img)
            return img_serializer.data
        return no_image_url  # 디폴트 경로를 반환합니다.



class CommentsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    replies = RecursiveField(many=True,required=False)
    class Meta:
        model = Comments
        fields = '__all__'
        
class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    class Meta:
        model = Post
        fields = '__all__'
        
        
