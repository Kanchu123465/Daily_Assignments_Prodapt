from rest_framework import fields, serializers
from donors.models import Donors
class DonorsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Donors
        fields=('bloodgroup','name','address','pincode','mblno','lastdonateddate')