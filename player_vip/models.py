from django.db import models
from players.models import Player  # Certifique-se que o nome do app onde está o Player é 'player'

class PlayerVIP(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='vips')
    active = models.BooleanField(default=False)
    tier = models.IntegerField()
    expiration = models.IntegerField()
    vip_days = models.IntegerField()
    type_vip = models.IntegerField()
    warnings = models.IntegerField()

    def __str__(self):
        return f"VIP - {self.player} (Tier {self.tier})"
