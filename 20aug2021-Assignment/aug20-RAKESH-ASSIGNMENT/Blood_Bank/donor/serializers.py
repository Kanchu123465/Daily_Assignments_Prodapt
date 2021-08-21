from rest_framework import serializers
from donor.models import Donor

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Donor
        fields=["blood_group","donor_name","address","pincode","Mobile_no","last_donated_date"]