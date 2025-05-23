from django.db import models
from seasons.models import Season
from players.models import Player

# Modelo SEASON_PLAYER
class SeasonPlayer(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    
    pontos = models.IntegerField(null=True, blank=True)
    elo = models.IntegerField(null=True, blank=True)
    MMR = models.FloatField(null=True, blank=True)
    sigma = models.FloatField(null=True, blank=True)
    win = models.IntegerField(null=True, blank=True)
    lose = models.IntegerField(null=True, blank=True)
    win_streak = models.IntegerField(null=True, blank=True)
    mvp = models.IntegerField(null=True, blank=True)
    queue = models.IntegerField(null=True, blank=True)

    class Meta:
        unique_together = ('season', 'player')

    def __str__(self):
        return f"{self.player.inhouse_nickname} - Season {self.season.season}"