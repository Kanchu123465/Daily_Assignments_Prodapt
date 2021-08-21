from django.db import models

# Create your models here.
class Donors(models.Model):
    bloodgroup=models.CharField(max_length=20)
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    pincode=models.IntegerField()
    mblno=models.BigIntegerField()
    lastdonateddate=models.DateField()