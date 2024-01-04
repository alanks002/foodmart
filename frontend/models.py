from django.db import models

# Create your models here.

class contactdb(models.Model):
    Name=models.CharField(max_length=50,null=True,blank=True)
    Email=models.EmailField(max_length=50,null=True,blank=True)
    Subject=models.CharField(max_length=50,null=True,blank=True)
    Messege=models.CharField(max_length=100,null=True,blank=True)



class singinupdb(models.Model):
    Username=models.CharField(max_length=50,null=True,blank=True)
    Email=models.EmailField(max_length=50,null=True,blank=True)
    Password=models.CharField(max_length=50,null=True,blank=True)

class cartdb(models.Model):
    name=models.CharField(max_length=50,null=True,blank=True)
    product_Name=models.CharField(max_length=50,null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Total=models.IntegerField(null=True,blank=True)

class CheckoutDB(models.Model):
    firstnm = models.CharField(max_length=100, null=True, blank=True)
    lastnm = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)