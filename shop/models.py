from django.db import models
from django.utils import timezone
from account.models import User , Address
from product.models import Nutraceuticals


class RegularDelivery(models.Model):
    id = models.BigAutoField(primary_key=True)
    request_date = models.DateTimeField(default=timezone.now)
    delivery_state = models.CharField(max_length=100)
    products = models.ForeignKey(Nutraceuticals, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='member_id')

    class Meta:
        managed = True
        db_table = 'regular_delivery'
        

class ShoppingCart(models.Model):
    id = models.BigAutoField(primary_key=True),
    product= models.ForeignKey(Nutraceuticals, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='member_id')

    class Meta:
        managed = True
        db_table = 'shopping_cart'
        
class Order(models.Model):
    id = models.BigAutoField(primary_key=True),
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='member_id')
    ordered_date = models.DateTimeField(default=timezone.now)
    total_price = models.IntegerField(default=0)
    status = models.CharField(max_length=50)
    class Meta:
        managed = True
        db_table = 'order'
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Nutraceuticals, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    
    class Meta:
        managed = True
        db_table = 'order_item'