from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

star = models.IntegerField(
    default=0,
    validators=[MaxValueValidator(5), MinValueValidator(0)]
)

import datetime

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    



class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=100)
     



    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, default='',blank=True, null=True)
    price = models.DecimalField(default= 0, max_digits=10, decimal_places=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1 )
    image = models.ImageField(upload_to='upload/products/', blank=True, null=True)
    star = models.IntegerField(default=0,validators=[MaxValueValidator(5), MinValueValidator(0)])
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=0,max_digits=12)
     
    # type_size =(
    #     ('small', 32),
    #     ('medium', 42),
    #     ('large', 52),
    # )
    # size = models.CharField(max_length=10, choices=type_size, default=32)


    def __str__(self):
        return self.name
    

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(default='', max_length=500, blank=False)
    phone = models.CharField( max_length=15, blank=False)
    date = models.DateTimeField(default=datetime.datetime.now, blank=True)
    status = models.BooleanField( default=False)

    def __str__(self):
        return self.name