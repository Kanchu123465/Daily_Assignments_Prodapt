from django.db import models

# Create your models here.
class Donar(models.Model):
    name=models.CharField(max_length=50)
    bloodgroup=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    pincode=models.IntegerField()
    mobnum=models.BigIntegerField()
    lastdonated_date=models.IntegerField()
