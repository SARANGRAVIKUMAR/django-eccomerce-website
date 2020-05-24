from django.db import models

from home.models import Product


class CartItem(models.Model):
    cart = models.ForeignKey("Cart",null = True,blank= True,on_delete = models.CASCADE)
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 1)
    line_total = models.DecimalField(max_digits = 10,decimal_places = 2,default = 10.99)

    def __str__(self):
        return self.product.title



class Cart(models.Model):
    
    quantity = models.IntegerField(default=1)

    total = models.DecimalField(max_digits=10, decimal_places=2,default=0.0)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "cart id %s" % (self.id)

