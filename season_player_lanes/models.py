from django.db import models
from players.models import Player
from seasons.models import Season

class SeasonPlayerLane(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    queue = models.IntegerField(null=True, blank=True)

    blue_win = models.IntegerField(default=0)
    blue_lose = models.IntegerField(default=0)
    red_win = models.IntegerField(default=0)
    red_lose = models.IntegerField(default=0)

    top_win = models.IntegerField(default=0)
    top_lose = models.IntegerField(default=0)
    jg_win = models.IntegerField(default=0)
    jg_lose = models.IntegerField(default=0)
    mid_win = models.IntegerField(default=0)
    mid_lose = models.IntegerField(default=0)
    adc_win = models.IntegerField(default=0)
    adc_lose = models.IntegerField(default=0)
    sup_win = models.IntegerField(default=0)
    sup_lose = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.player} - Season {self.season} - Queue {self.queue}"
