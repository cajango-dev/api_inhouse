from rest_framework import serializers
from .models import Match
from player_matches.models import PlayerMatch


class MatchListSerializer(serializers.ModelSerializer):
    season = serializers.StringRelatedField()

    class Meta:
        model = Match
        fields = ['match_id', 'season', 'start_time', 'end_time', 'winner']

class MatchDetailSerializer(serializers.ModelSerializer):
    players = serializers.SerializerMethodField()

    class Meta:
        model = Match
        fields = [
            'match_id', 'season', 'status', 'start_time', 'end_time',
            'winner', 'mmr_blue', 'mmr_red',
            'blue_captain', 'red_captain', 'match_found_id', 'category_id',
            'thread_log_id', 'queue', 'staff_calls', 'history_msg',
            'draftlol_room', 'draftlol_password', 'draftlol_start',
            'webhook_lobby', 'webhook_blue', 'webhook_red',
            'draft_ended', 'players'
        ]

    def get_players(self, obj):
        player_matches = PlayerMatch.objects.filter(match=obj).select_related('player')
        return [
            {
                "player_id": pm.player.player_id,
                "discord_id": int(pm.player.discord_id),
                "team": pm.team,
                "win": "true" if pm.win else "false",
                "champion": pm.champion,
                "lane": pm.lane,
                "captain": "true" if pm.captain else "false"
            }
            for pm in player_matches
        ]

class MatchListWithPlayersSerializer(MatchDetailSerializer):
    pass  # herdando tudo de MatchDetailSerializer
