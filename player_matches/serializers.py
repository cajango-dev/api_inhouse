from rest_framework import serializers
from .models import PlayerMatch

class PlayerMatchListSerializer(serializers.ModelSerializer):
    match = serializers.StringRelatedField()
    player = serializers.StringRelatedField()

    class Meta:
        model = PlayerMatch
        fields = ['match', 'player']

class PlayerMatchDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerMatch
        fields = '__all__'

class PlayerMatchNestedSerializer(serializers.ModelSerializer):
    player_id = serializers.IntegerField(source='player.player_id')
    discord_id = serializers.IntegerField(source='player.discord_id')
    win = serializers.SerializerMethodField()
    captain = serializers.SerializerMethodField()

    class Meta:
        model = PlayerMatch
        fields = ['player_id', 'discord_id', 'team', 'win', 'champion', 'lane', 'captain']

    def get_win(self, obj):
        return "true" if obj.win else "false"

    def get_captain(self, obj):
        return "true" if obj.captain else "false"
