from rest_framework import serializers
from  django.db.models import fields
from donors.models import donors

class donSerializer(serializers.ModelSerializer):
    class Meta:
        model = donors
        fields = ('bldgrp', 'donorname','donoradd', 'pincode', 'mobile', 'lastblddonate')

        