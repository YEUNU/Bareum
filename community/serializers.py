from rest_framework import serializers
from .models import Post, Comments, User, PostImage
from rest_framework_recursive.fields import RecursiveField
from account.models import ProfileImage
from account.serializer import ProfileSerializer


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = "__all__"
    
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
    user = UserSerializer(read_only=True)
    post_image = PostImageSerializer(read_only=True)
    post_images = serializers.SerializerMethodField()  # 새로운 필드를 추가하세요.

    class Meta:
        model = Post
        fields = '__all__'

    def get_post_images(self, obj):
        images = PostImage.objects.filter(post=obj).first()
        if images:  # 이미지가 있는 경우만 반환합니다.
            img_serializer = PostImageSerializer(images)
            return img_serializer.data
        else:
            return 'default_img'
        
        
