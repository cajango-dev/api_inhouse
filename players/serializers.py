from rest_framework import serializers
from .models import Player

class PlayerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['player_id', 'discord_id', 'inhouse_nickname', 'elo_lol']

class PlayerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'
