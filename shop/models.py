from django.db import models
from django.utils import timezone
from account.models import User , Address
from product.models import Nutraceuticals


class RegularDelivery(models.Model):
    id = models.BigAutoField(primary_key=True)
    request_date = models.DateTimeField(default=timezone.now)
    delivery_state = models.CharField(max_length=100)
    products = models.ForeignKey(Nutraceuticals,max_length=100,many=True)
    address = models.ForeignKey(Address,models.DO_NOTHING,)
    user = models.ForeignKey(User, models.DO_NOTHING,db_column='member_id')


    class Meta:
        managed = True
        db_table = 'regular_delivery'