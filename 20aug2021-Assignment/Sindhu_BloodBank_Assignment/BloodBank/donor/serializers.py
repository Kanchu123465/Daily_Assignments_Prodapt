from rest_framework import serializers
from donor.models import Donor

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Donor
        fields=('name','bloodgroup','address','pincode','phoneno','last_donated_date')