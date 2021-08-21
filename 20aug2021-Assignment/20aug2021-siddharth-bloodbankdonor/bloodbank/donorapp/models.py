from django.db import models

# Create your models here.
class Donor(models.Model):
    bloodgroup=models.CharField(max_length=50,default='')
    name=models.CharField(max_length=50,default='')
    address=models.CharField(max_length=50,default='')
    pincode=models.CharField(max_length=50,default='')
    phone=models.CharField(max_length=50,default='')
    lastdonateddate=models.DateField(max_length=50,default='')
#{"bloodgroup":"A+","name":"Siddharth","address":"Sagar","pincode":"470002","phone":"9425171349","lastdonateddate":"2020-09-08"}