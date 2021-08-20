from django.db import models
from django.db.models import fields
from rest_framework import serializers
from Donor.models import Donor1

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Donor1
        fields=('name','address','bloodgroup','mobileno','lastdonateddate','pincode')