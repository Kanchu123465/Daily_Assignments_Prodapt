from django.db import models

# Create your models here.
class Blood(models.Model):
    blood_group = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    pincode = models.IntegerField()
    mobile_num = models.BigIntegerField()
    last_date = models.DateField()

