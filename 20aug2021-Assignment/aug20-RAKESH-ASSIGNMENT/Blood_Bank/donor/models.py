from django.db import models

# Create your models here.
class Donor(models.Model):
    blood_group=models.CharField(max_length=50)
    donor_name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    pincode=models.IntegerField()
    Mobile_no=models.BigIntegerField()
    last_donated_date=models.DateField()
   
