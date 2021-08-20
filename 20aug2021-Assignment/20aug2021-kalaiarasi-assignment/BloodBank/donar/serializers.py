from rest_framework import serializers
from donar.models import Donar

class DonarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Donar
        fields=('name','bloodgroup','address','pincode','mobnum','lastdonated_date')
