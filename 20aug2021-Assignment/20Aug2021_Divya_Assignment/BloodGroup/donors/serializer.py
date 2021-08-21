from rest_framework import serializers
from donors.models import Donors

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donors
        fields = ("blood_group","name","address","pincode","mobile_no","last_donated_date")