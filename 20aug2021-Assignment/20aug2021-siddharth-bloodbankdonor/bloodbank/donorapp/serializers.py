from rest_framework import serializers
from donorapp.models import Donor

class DonorSerializers(serializers.ModelSerializer):
    class Meta:
        model=Donor
        fields=("bloodgroup","name","address","pincode","phone","lastdonateddate")