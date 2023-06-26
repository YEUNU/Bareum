from django.db import models

# Create your models here.

class eating_Nutraceuticals(models.Model): 
    checking_number = models.BigAutoField(primary_key=True)
    nutraceuticals_name = models.CharField(max_length=100)
    login_id = models.CharField(max_length=150)

    class Meta:
        managed = True
        db_table = 'eating_nutraceuticals'
