from django.db.models import fields
from Donors.models import Donor
from rest_framework import serializers
class Donorserializers(serializers.ModelSerializer):
    class Meta:
        model=Donor
        fields=('dname','bloodg','address','pincode','mobile','lastdonate')