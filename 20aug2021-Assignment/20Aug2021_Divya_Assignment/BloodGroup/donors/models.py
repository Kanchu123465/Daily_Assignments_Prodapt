from django.db import models
from django.db.models.fields import BigIntegerField, CharField,IntegerField

# Create your models here.
class Donors(models.Model):
    blood_group = CharField(max_length=50)
    name = CharField(max_length=50)
    address = CharField(max_length=50)
    pincode = IntegerField(default=False)
    mobile_no = BigIntegerField(default=False)
    last_donated_date = CharField(max_length=50)
    