from django.db import models

# Create your models here.
class Donor1(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    bloodgroup=models.CharField(max_length=50)
    mobileno=models.BigIntegerField()
    lastdonateddate=models.DateField()
    pincode=models.IntegerField()