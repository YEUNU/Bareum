from django.db import models
from account.models import User
# Create your models here.
class Post(models.Model):
    post_id = models.IntegerField(primary_key=True)
    post_date = models.DateField()
    post_title = models.CharField(max_length=100)
    post_contents = models.CharField(max_length=100)
    post_like = models.IntegerField()
    post_category = models.CharField(max_length=9)
    user = models.ForeignKey(User, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'post'

class Comments(models.Model):
    comments_id = models.IntegerField(primary_key=True)
    comment_date = models.DateField()
    comment_contents = models.CharField(max_length=100)
    comment_like = models.IntegerField()
    post = models.ForeignKey('Post', models.DO_NOTHING)
    user = models.ForeignKey(User, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'comments'
        
class test(models.Model):
    test_id = models.IntegerField(primary_key=True)
    test_date = models.DateField()
    test_contents = models.CharField(max_length=100)
    test_like = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'test'