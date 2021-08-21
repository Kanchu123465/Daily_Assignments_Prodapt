from django.db.models.base import Model
from rest_framework import serializers
from donors.models import Blood
from django.db.models import fields

class BloodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blood
        fields = ("blood_group","name","address","pincode","mobile_num","last_date")