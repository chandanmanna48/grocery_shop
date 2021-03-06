from django.db import models

# Create your models here.
class Product(models.Model):
    quality =(
        ('Good','Good'),
        ('Better','Better'),
        ('Best','Best'),
    )
    category = (
        ('Grocery','Grocery'),
        ('Foods','Foods'),
        ('Vegetable','Vegetable'),
        ('Medicine','Medicine'),
        ('Clothes','Clothes'),
        ('Beauty_products','Beauty_products'),
        ('Drinks','Drinks'),
        ('Fruits','Fruits'),
    )
    boolean = (
        ('True','True'),
        ('False','False'),
    )

    name = models.CharField(max_length=30,null=False,blank=False)
    brand = models.CharField(max_length=15,null=True,blank=True)
    discount_price = models.CharField(max_length=10,null=True,blank=True)
    actual_price = models.CharField(max_length=10,null=True,blank=True)
    discount_percentage = models.CharField(max_length=15,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='product_images',null=True,blank=True)
    quality = models.CharField(max_length=15,null=True,blank=True,choices=quality)
    category = models.CharField(max_length=20,null=True,blank=True,choices=category)
    special_offer = models.CharField(max_length=20,null=True,blank=True,choices=boolean)
    best_offer = models.CharField(max_length=20,null=True,blank=True,choices=boolean)

    def __str__(self):
        return self.name