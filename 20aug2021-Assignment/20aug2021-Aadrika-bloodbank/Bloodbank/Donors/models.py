from django.db import models

# Create your models here.
class Donor(models.Model):
    dname=models.CharField(max_length=50)
    bloodg=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    pincode=models.BigIntegerField()
    mobile=models.BigIntegerField()
    lastdonate=models.DateField()
