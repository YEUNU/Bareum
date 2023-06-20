from rest_framework import serializers
from .models import Post, Comments, User
from rest_framework_recursive.fields import RecursiveField
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_name']
        
class CommentsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    replies = RecursiveField(many=True,required=False)
    class Meta:
        model = Comments
        fields = '__all__'