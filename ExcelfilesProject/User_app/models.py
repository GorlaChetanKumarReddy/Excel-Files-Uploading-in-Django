from django.db import models

class Files_Data(models.Model):
    fdid = models.AutoField(primary_key=True)
    BANK = models.CharField(max_length=150,null=True,blank=True)
    IFSC = models.CharField(max_length=150,null=True,blank=True)
    MICR = models.CharField(max_length=150,null=True,blank=True)
    BRANCH = models.CharField(max_length=150,null=True,blank=True)
    ADDRESS = models.TextField(null=True,blank=True)
    CITY1 = models.CharField(max_length=200,null=True,blank=True)
    CITY2 = models.CharField(max_length=200,null=True,blank=True)
    STATE = models.CharField(max_length=200,null=True,blank=True)
    STD = models.CharField(max_length=100,null=True,blank=True)
    PHONE = models.CharField(max_length=150,null=True,blank=True)
    DateTime = models.DateTimeField(auto_now_add=True)