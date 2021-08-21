from django.db import models

# Create your models here.
class Donar(models.Model):
    bloodgroup=models.CharField(max_length=50)
    donarname=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    mobilenumber=models.BigIntegerField()
    pincode=models.BigIntegerField()
    lastdonatedate=models.DateField()
    