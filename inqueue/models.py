from django.db import models
from players.models import Player  # assumindo app players

class InQueue(models.Model):
    jogo = models.TextField()
    fk_player = models.ForeignKey('players.Player', to_field='player_id', on_delete=models.CASCADE)
    fk_discord_id = models.IntegerField(unique=True)
    display_name = models.TextField()
    entrou_timestamp = models.BigIntegerField()
    elo = models.IntegerField()
    mmr = models.IntegerField()
    sigma = models.IntegerField()
    achou_fila = models.IntegerField()
    match_found_id = models.TextField(null=True, blank=True)
    player_aceitou_fila = models.IntegerField()
    queue = models.TextField()
    lane = models.IntegerField()
    secret_queue = models.IntegerField()
    do_not_call = models.IntegerField()
    not_be_captain = models.IntegerField()
    priority = models.IntegerField()
    match_found_link = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'INQUEUE'

    def __str__(self):
        return self.display_name
