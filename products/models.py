from django.db import models
from users.models import User
from django.utils import timezone
import datetime



class Product_Category(models.Model):
    products = models.ManyToManyField('Product', blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class product(models.Model):
    Owner = models.ForeignKey(User, on_delete=models.CASCADE)
    sold_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='sold_to')
    Name=models.CharField(max_length=100)
    Description=models.TextField()
    image = models.ImageField(upload_to='images/products/', default='product.jpg')
    Bid_start_price = models.IntegerField()
    Bid_Current_price = models.IntegerField()
    price = models.IntegerField(null=True, blank=True)
    product_status = (
        ('A', 'Active'),
        ('S', 'Sold'),


    )
    status = models.CharField(max_length=100, default='open')
    last_bid_time = models.DateTimeField()
    fav_users = models.ManyToManyField(User, blank=True , related_name='fav_users')

    def __str__(self):
        return self.Name



    

    