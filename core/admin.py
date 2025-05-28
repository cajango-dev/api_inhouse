from django.contrib import admin
from champions.models import Champion
from champion_tier_list.models import ChampionTierList
from players.models import Player
from inqueue.models import InQueue
from player_matches.models import PlayerMatch
from season_player_lanes.models import SeasonPlayerLane
from season_players.models import SeasonPlayer
from matches.models import Match
from seasons.models import Season
from staff.models import Staff

@admin.register(Champion)
class ChampionAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
    search_fields = ('id','name',)

@admin.register(ChampionTierList)
class ChampionTierListAdmin(admin.ModelAdmin):
    list_display = ('champion', 'queue', 'pick_blue', 'pick_red', 'ban_blue', 'ban_red')
    list_filter = ('queue',)
    search_fields = ('champion__name',)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('inhouse_nickname', 'discord_id', 'lol_id', 'elo_lol', 'rank_lol', 'riot_verified', 'ingame')
    search_fields = ('inhouse_nickname', 'discord_id', 'lol_id')
    list_filter = ('riot_verified', 'ingame')

@admin.register(InQueue)
class InQueueAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'fk_discord_id', 'elo', 'mmr', 'queue', 'lane', 'entrou_timestamp')
    search_fields = ('display_name',)
    list_filter = ('queue', 'lane')

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('match_id', 'season', 'status', 'start_time', 'end_time', 'winner')
    search_fields = ('match_id',)
    list_filter = ('status', 'season')

@admin.register(PlayerMatch)
class PlayerMatchAdmin(admin.ModelAdmin):
    list_display = ('player', 'match', 'team', 'captain', 'lane', 'win', 'mvp', 'champion', 'mmr')
    search_fields = ('player__inhouse_nickname', 'match__match_id')
    list_filter = ('team', 'captain', 'win')

@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('season', 'status', 'start', 'end', 'on_off')
    list_filter = ('status', 'on_off')

@admin.register(SeasonPlayerLane)
class SeasonPlayerLaneAdmin(admin.ModelAdmin):
    list_display = ('player', 'season', 'queue', 'blue_win', 'blue_lose', 'red_win', 'red_lose')
    search_fields = ('player__inhouse_nickname',)
    list_filter = ('queue',)

@admin.register(SeasonPlayer)
class SeasonPlayerAdmin(admin.ModelAdmin):
    list_display = ('player', 'season', 'pontos', 'elo', 'MMR', 'sigma', 'win', 'lose', 'win_streak', 'mvp', 'queue')
    search_fields = ('player__inhouse_nickname',)
    list_filter = ('queue',)

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('discord_user', 'discord_id', 'email', 'level')
    search_fields = ('discord_user', 'email')
    list_filter = ('level',)
