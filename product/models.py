from django.db import models

from account.models import User

class Company(models.Model):

    company_id = models.BigAutoField(primary_key=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'company'




class Nutraceuticals(models.Model): 
    업체별_제품코드= models.CharField(max_length=20,primary_key=True,default="미등록")
    업체코드 = models.CharField(max_length=20,default="미등록")
    제품코드 = models.CharField(max_length=20,default="미등록")    
    nutraceuticals_name = models.CharField(max_length=100)
    섭취시주의사항 = models.TextField()
    업소명 = models.TextField()
    섭취방법 = models.TextField()
    주된기능성 = models.TextField()
    유통기한 = models.TextField()
    보관방법 = models.TextField()
    원재료 = models.TextField()
    비타민D = models.FloatField(max_length=10)
    비타민E = models.FloatField(max_length=10)
    비타민k = models.FloatField(max_length=10)
    비타민B1 = models.FloatField(max_length=10) 
    비타민B2 = models.FloatField(max_length=10)
    나이아신 = models.FloatField(max_length=10)
    비타민B6 = models.FloatField(max_length=10)
    엽산 = models.FloatField(max_length=10)
    비타민B12 = models.FloatField(max_length=10)
    비오틴 = models.FloatField(max_length=10)
    비타민C = models.FloatField(max_length=10)
    칼슘 = models.FloatField(max_length=10)
    마그네슘 = models.FloatField(max_length=10)
    철 = models.FloatField(max_length=10)
    아연 = models.FloatField(max_length=10)
    구리 = models.FloatField(max_length=10)
    셀레늄_셀렌 = models.FloatField(max_length=10)
    요오드 = models.FloatField(max_length=10)
    망간 = models.FloatField(max_length=10)
    몰리브덴 = models.FloatField(max_length=10)
    칼륨 = models.FloatField(max_length=10)
    식이섬유 = models.FloatField(max_length=10)
    단백질 = models.FloatField(max_length=10)
    프로바이오틱스 = models.FloatField(max_length=10)
    진세노사이드 = models.FloatField(max_length=10)
    루테인 = models.FloatField(max_length=10)
    EPA_DHA_Sum= models.FloatField(max_length=10)
    비타민A= models.FloatField(max_length=10)
    ad = models.BooleanField(default=False)



    class Meta:
        managed = True
        db_table = 'nutraceuticals'
        




class Review(models.Model):
    제품코드 = models.ForeignKey(Nutraceuticals,on_delete=models.CASCADE)
    online_review_number = models.BigAutoField(primary_key=True)
    nutraceuticals_name = models.CharField(unique=True,max_length=100)
    company_name = models.CharField(max_length=100, null=True)
    lowest = models.IntegerField()
    reviews = models.TextField()
    total_reviews = models.IntegerField()
    average_rating = models.FloatField()
    class Meta:

        managed = True
        db_table = 'review'

class new_Nutraceuticals(models.Model): 
    input_number = models.BigAutoField(primary_key=True)
    nutraceuticals_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='new_Nutraceuticals/')
    class Meta:
        managed = True
        db_table = 'new_nutraceuticals'
    
class BareumReview(models.Model):
    제품코드 = models.ForeignKey(Nutraceuticals,on_delete=models.CASCADE)
    bareum_review_number = models.BigAutoField(primary_key=True)
    nutraceuticals_name = models.CharField(unique=True,max_length=100)
    company_name = models.CharField(max_length=100, null=True)
    reviews = models.TextField()
    rating = models.FloatField()
    review_img_url = models.ImageField(upload_to='review_images/')
    writer = models.ForeignKey(User,models.DO_NOTHING,db_column='member_id')
    class Meta:

        managed = True
        db_table = 'bareum_review'
