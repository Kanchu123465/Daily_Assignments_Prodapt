from rest_framework import serializers
from Donar.models import Donar

class donarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Donar
        fields=('bloodgroup','donarname','address','mobilenumber','pincode','lastdonatedate')