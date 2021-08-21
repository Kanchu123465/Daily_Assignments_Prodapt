from django.db import models

# Create your models here.
class Donorapp1(models.Model):
    bloodgroup = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=30)
    pincode=models.IntegerField()
    phone=models.BigIntegerField()
    last_donate_date=models.DateField()
    