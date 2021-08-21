from django.db import models

class Donors(models.Model):

    bgroup = models.CharField(max_length=50)
    dname = models.CharField(max_length=50)
    daddress = models.CharField(max_length=50)
    dpincode = models.IntegerField()
    dmobno = models.BigIntegerField()
    dlastdate = models.DateField()
