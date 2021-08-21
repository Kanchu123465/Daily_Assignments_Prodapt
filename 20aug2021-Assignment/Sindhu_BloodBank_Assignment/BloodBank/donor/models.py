from django.db import models

# # Create your models here.
class Donor(models.Model):
    name=models.CharField(max_length=50)
    bloodgroup=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    pincode=models.IntegerField()
    phoneno=models.BigIntegerField()
    last_donated_date=models.DateField()
