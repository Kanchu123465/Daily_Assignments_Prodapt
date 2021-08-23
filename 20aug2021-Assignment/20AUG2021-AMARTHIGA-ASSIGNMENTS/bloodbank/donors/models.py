from django.db import models

# Create your models here.
class donors(models.Model):
    bldgrp = models.CharField(max_length=50, default = '')
    donorname = models.CharField(max_length=50, default = '')
    donoradd = models.CharField(max_length=50, default = '')
    pincode = models.IntegerField(default='')
    mobile = models.BigIntegerField(default='')
    lastblddonate = models.CharField(max_length=50, default = '')
    