from rest_framework import serializers
from .models import SeasonPlayerLane

class SeasonPlayerLaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeasonPlayerLane
        fields = '__all__'
