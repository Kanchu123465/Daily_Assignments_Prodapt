from django.db import models
class Doon(models.Model):
   bloodgroup=models.CharField(max_length=25)
   name =models.CharField(max_length=50)
   address =models.CharField(max_length=50)
   pincode=models.CharField(max_length=25)
   mobileno=models.BigIntegerField()
   last_donated_date=models.CharField(max_length=50)

