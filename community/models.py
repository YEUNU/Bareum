from django.db import models
from account.models import User
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    post_id = models.BigAutoField(primary_key=True)
    post_date = models.DateTimeField(default=timezone.now)
    post_title = models.CharField(max_length=100)
    post_contents = models.CharField(max_length=100)
    post_like = models.IntegerField()
    post_category = models.CharField(max_length=9)
    user = models.ForeignKey(User, models.DO_NOTHING,db_column='member_id')

    class Meta:
        managed = True
        db_table = 'post'

class Comments(models.Model):
    comments_id = models.BigAutoField(primary_key=True)
    comment_date = models.DateTimeField(default=timezone.now)
    comment_contents = models.CharField(max_length=100)
    comment_like = models.IntegerField()
    post = models.ForeignKey('Post', models.DO_NOTHING)
    user = models.ForeignKey(User, models.DO_NOTHING,db_column='member_id')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    class Meta:
        managed = True
        db_table = 'comments'
    
class PostImage(models.Model):
    image = models.ImageField(upload_to='images/')  # 이미지 저장할 위치
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # 외래키로 게시물(Post) 연결
