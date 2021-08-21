from rest_framework import serializers
from donar.models import donar

class DonarSerializer(serializers.ModelSerializer):
    class Meta:
        model=donar
        fields=('name','bloodgroup','adress','pincode','phoneno','LDD')