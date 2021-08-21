from django.db import models

# Create your models here.
class donar(models.Model):
    name=models.CharField(max_length=50)
    bloodgroup=models.CharField(max_length=100)
    adress=models.CharField(max_length=50)
    pincode=models.IntegerField()
    phoneno=models.BigIntegerField()
    LDD=models.DateField()
