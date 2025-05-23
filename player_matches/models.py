from django.db import models
from players.models import Player
from matches.models import Match

# Modelo PlayerMatch (Partida de Players)
class PlayerMatch(models.Model):
    match = models.ForeignKey(Match, to_field='match_id', on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)

    team = models.IntegerField(null=True, blank=True)
    captain = models.BooleanField(default=False)
    lane = models.IntegerField(null=True, blank=True)
    win = models.IntegerField(null=True, blank=True)
    mvp = models.IntegerField(null=True, blank=True)
    champion = models.IntegerField(null=True, blank=True)
    mmr = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.player.inhouse_nickname} in match {self.match.match_id}"
