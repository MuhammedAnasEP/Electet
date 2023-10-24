from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categorys(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    slug = models.SlugField()

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to ='photo')
    image1 = models.ImageField(upload_to ='photo',default=0, null = True)
    image2 = models.ImageField(upload_to ='photo',default=0, null = True)
    image3 = models.ImageField(upload_to ='photo',default=0, null = True)
    price = models.FloatField()
    stock = models.IntegerField()
    category = models.ForeignKey(Categorys, on_delete=models.CASCADE)
    slug = models.SlugField()
    description=models.CharField(max_length=200, null = True)
    company = models.CharField(max_length=100)

    def __str__(self) :
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)    
    city = models.CharField(max_length=200) 
    district = models.CharField(max_length=200) 
    state = models.CharField(max_length=200)
    pincode = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    pname = models.CharField(max_length=100)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered')], default='pending')

# class ProductRecommendation(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey('home.Products', on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.user} - {self.product}'


