from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def _create_user(self, login_id, password=None, **extra_fields):
        if not login_id:
            raise ValueError('The Login ID must be set')
        login_id = self.normalize_email(login_id)
        user = self.model(login_id=login_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, login_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(login_id, password, **extra_fields)

    def create_superuser(self, login_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(login_id, password, **extra_fields)

class User(AbstractUser):
    member_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='member_id')
    nickname = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    birthday = models.DateField(null=True)
    height = models.FloatField(null=True)
    weight = models.FloatField(null=True)
    gender = models.CharField(max_length=100, null=True)
    first_name = None
    last_name = None

    username = None

    # login_id 필드 추가
    login_id = models.CharField(unique=True, max_length=150, verbose_name='login ID')

    USERNAME_FIELD = 'login_id'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    USERNAME_FIELD = 'login_id'
    class Meta:
        managed = True
        db_table = 'user'
        swappable = "AUTH_USER_MODEL"
        
        
class HealthInfo(models.Model):
    health_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING,db_column='member_id')

    class Meta:
        managed = True
        db_table = 'health_info'

class ProfileImage(models.Model):
    image = models.ImageField(upload_to='profile_images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    postcode = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    extra_address = models.CharField(max_length=255, blank=True)
    detailed_address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50, blank=True)
    receiver = models.CharField(max_length=50,blank=True)        
    
    
class SearchLog(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    word = models.CharField(max_length=255)
    
    class Meta:
        managed = True
        db_table = 'search_log'