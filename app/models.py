from django.db import models

class Students(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    phnumber=models.CharField(max_length=20)
    altphnumber=models.CharField(max_length=20)
    college=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
class Kathabooks(models.Model):
    phnumber=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    timeofday=models.CharField(max_length=20)
    amount=models.CharField(max_length=255)

