from django.db import models

# Create your models here.
class Products(models.Model):
    product_number = models.CharField(max_length=10, null=False)
    product_name = models.CharField(max_length=50, null=False,default="")
    desc = models.CharField(max_length=300,blank=True,default="")
    price =  models.IntegerField(default = 0)
    image = models.ImageField(upload_to="mylist/images", default="")

    def __str__(self):
        return self.product_name

class Cart(models.Model):
    product_number = models.CharField(max_length=10, null=False)
    product_name = models.CharField(max_length=50, null=False,default="")
    desc = models.CharField(max_length=300,blank=True,default="")
    date = models.DateField(null=True)
    price =  models.IntegerField(default = 0)
    image = models.ImageField(upload_to="mylist/images", default="")

    def __str__(self):
        return self.product_name
    