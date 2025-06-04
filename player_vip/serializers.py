from rest_framework import serializers
from .models import PlayerVIP

class PlayerVIPSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerVIP
        fields ='__all__'