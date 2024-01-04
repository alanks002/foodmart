from django.db import models

# Create your models here.
class fooddb(models.Model):

    Name=models.CharField(max_length=50,null=True,blank=True)
    Description=models.EmailField(max_length=100,null=True,blank=True)
    Profile=models.ImageField(upload_to="img", null=True,blank=True)


class prodb(models.Model):
    Product_Name=models.CharField(max_length=50,null=True,blank=True)
    Product_Category=models.CharField(max_length=50,null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Description=models.CharField(max_length=50,null=True,blank=True)
    Profile=models.ImageField(upload_to="img", null=True,blank=True)
