from django.db import models
from champions.models import Champion

class ChampionTierList(models.Model):
    queue = models.IntegerField()
    champion = models.ForeignKey(Champion, on_delete=models.CASCADE)
    pick_blue = models.IntegerField(default=0)
    pick_red = models.IntegerField(default=0)
    ban_blue = models.IntegerField(default=0)
    ban_red = models.IntegerField(default=0)
    win_blue = models.IntegerField(default=0)
    win_red = models.IntegerField(default=0)
    lose_blue = models.IntegerField(default=0)
    lose_red = models.IntegerField(default=0)
    pick_top = models.IntegerField(default=0)
    pick_jg = models.IntegerField(default=0)
    pick_mid = models.IntegerField(default=0)
    pick_adc = models.IntegerField(default=0)
    pick_sup = models.IntegerField(default=0)
    first_pick = models.IntegerField(default=0)
    last_pick = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.champion.name} - Queue {self.queue}"

