from rest_framework import serializers
from Donor.models import Doon
class DoonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doon
        fields=("bloodgroup","name","address","pincode","mobileno","last_donated_date")