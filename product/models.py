from django.db import models
from account.models import User
class Company(models.Model):
    company_id = models.BigAutoField(primary_key=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'company'



class Ingredient(models.Model):
    ingredient_id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'ingredient'

class Nutraceuticals(models.Model):
    nutraceuticals_id = models.BigAutoField(primary_key=True)
    nutraceuticals_name = models.CharField(max_length=100)
    nutraceuticals_categroy = models.CharField(max_length=1)
    nutraceuticals_rating = models.IntegerField()
    nutraceuticals_effects = models.CharField(max_length=100)
    nutraceuticals_side_effects = models.CharField(max_length=100)
    nutraceuticals_company = models.CharField(max_length=100)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    ingredient = models.ForeignKey(Ingredient, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'nutraceuticals'


class UserReview(models.Model):
    user_review_id = models.BigAutoField(primary_key=True)
    review_rating = models.IntegerField()
    review_contents = models.CharField(max_length=500)
    user = models.ForeignKey(User, models.DO_NOTHING)
    nutraceuticals = models.ForeignKey(Nutraceuticals, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'user_review'
        
class OnelineReview(models.Model):
    online_review_id = models.BigAutoField(primary_key=True)
    review_rating = models.IntegerField()
    review_contents = models.CharField(max_length=500)
    nutraceuticals = models.ForeignKey(Nutraceuticals, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'oneline_review'

