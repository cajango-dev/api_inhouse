from rest_framework import serializers
from .models import SeasonPlayer

class SeasonPlayerListSerializer(serializers.ModelSerializer):
    season = serializers.StringRelatedField()
    player = serializers.StringRelatedField()

    class Meta:
        model = SeasonPlayer
        fields = ['season', 'player']

class SeasonPlayerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeasonPlayer
        fields = '__all__'
