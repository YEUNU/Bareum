from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_login_id = models.CharField(max_length=100)
    user_loing_password = models.CharField(max_length=100)
    user_age = models.IntegerField()
    user_name = models.CharField(max_length=100)
    user_weight = models.FloatField(blank=True, null=True)
    user_height = models.FloatField(blank=True, null=True)
    user_nickname = models.CharField(max_length=100)
    user_sex = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'user'
        swappable = "AUTH_USER_MODEL"
        
        
class HealthInfo(models.Model):
    health_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'health_info'
