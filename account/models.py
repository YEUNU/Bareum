from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_login_id = models.CharField(max_length=100)
    user_login_password = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    user_weight = models.FloatField(blank=True, null=True)
    user_height = models.FloatField(blank=True, null=True)
    user_nickname = models.CharField(max_length=100)
    user_sex = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'user'
        
        
class HealthInfo(models.Model):
    health_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'health_info'


# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# class CustomUserManager(BaseUserManager):
#     def create_user(self, user_id, user_login_id, user_login_password, user_name, user_nickname = None, user_age = None, user_sex = None, user_weight=None, user_height=None, **extra_fields):
#         #     if not user_login_id:
#         #     raise ValueError('Users must have a login id')
#         # if not user_name:
#         #     raise ValueError('Users must have a name')
#         # if not user_nickname:
#         #     raise ValueError('Users must have a nickname')
#         # if not user_sex:
#         #     raise ValueError('Users must have gender information')

#         user = self.model(
#             user_id = user_id,
#             user_login_id=user_login_id,
#             user_login_password=user_login_password,
#             user_name=user_name,
#             user_nickname=user_nickname,
#             user_sex=user_sex,
#             user_age=user_age,
#             user_weight=user_weight,
#             user_height=user_height,
#             **extra_fields
#         )

#         user.set_password(user_login_password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, user_login_id, user_login_password, user_name, user_age, user_nickname, user_sex, user_weight=None, user_height=None):
#         user = self.create_user(
#             user_login_id=user_login_id,
#             user_login_password=user_login_password,
#             user_name=user_name,
#             user_age=user_age,
#             user_nickname=user_nickname,
#             user_sex=user_sex,
#             user_weight=user_weight,
#             user_height=user_height,
#         )
#         user.is_admin = True
#         user.is_staff = True
#         user.save(using=self._db)
#         return user

# class User(AbstractBaseUser):
#     user_id           = models.IntegerField(primary_key=True)
#     user_login_id     = models.CharField(max_length=100, unique=True)
#     user_login_password = models.CharField(max_length=100)
#     user_age          = models.IntegerField()
#     user_name         = models.CharField(max_length=100)
#     user_weight       = models.FloatField(blank=True, null=True)
#     user_height       = models.FloatField(blank=True, null=True)
#     user_nickname     = models.CharField(max_length=100)
#     user_sex          = models.CharField(max_length=100)
#     date_joined       = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
#     last_updated      = models.DateTimeField(verbose_name='last updated', auto_now=True)
#     # django default fields
#     is_active         = models.BooleanField(default=True)
#     is_admin          = models.BooleanField(default=False)
#     is_staff          = models.BooleanField(default=False)
#     class Meta:
#         managed = True
#         db_table = 'user'
        
#     USERNAME_FIELD = 'user_login_id'
#     # REQUIRED_FIELDS = ['user_name', 'user_age', 'user_nickname', 'user_sex',]
#     REQUIRED_FIELDS = ['user_name', 'password']
#     objects = CustomUserManager()

#     def __str__(self):
#         return self.user_login_id

#     def has_perm(self, perm, obj=None):
#         return self.is_admin

#     def has_module_perms(self, app_label):
#         return True

#     @property
#     def get_full_name(self):
#         return self.user_name

#     @property
#     def get_short_name(self):
#         return self.user_nickname
