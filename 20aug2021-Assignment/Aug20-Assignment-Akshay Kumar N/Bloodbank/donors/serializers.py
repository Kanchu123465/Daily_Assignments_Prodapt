from django.db.models import fields
from rest_framework import serializers
from donors.models import Donors

class DonorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Donors
        fields = ('bgroup','dname','daddress','dpincode','dmobno','dlastdate')