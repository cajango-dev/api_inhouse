from rest_framework import serializers
from .models import Season

class SeasonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ['season']

class SeasonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'
