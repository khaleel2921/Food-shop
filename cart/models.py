from django.db import models
from shop.models import *

# Create your models here.
class cartlist(models.Model):
    cart_id=models.CharField(max_length=250,unique=True)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id
    
class items(models.Model):
    productcart=models.ForeignKey(products,on_delete=models.CASCADE)
    cart=models.ForeignKey(cartlist,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.productcart
    def total(self):
        return self.productcart.price*self.quantity