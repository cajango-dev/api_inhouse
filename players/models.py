from django.db import models

# Modelo Player
class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    discord_id = models.BigIntegerField(unique=True)
    inhouse_nickname = models.CharField(max_length=100, unique=True)
    type_nick_inhouse = models.IntegerField(null=True, blank=True)
    lol_id = models.CharField(max_length=100, unique=True)
    elo_lol = models.IntegerField(null=True, blank=True)
    peak_elo_lol = models.IntegerField(null=True, blank=True)
    peak_rank_lol = models.IntegerField(null=True, blank=True)
    rank_lol = models.IntegerField(null=True, blank=True)
    elo_inhouse = models.IntegerField(null=True, blank=True)
    rank_inhouse = models.IntegerField(null=True, blank=True)
    pdl_inhouse = models.IntegerField(null=True, blank=True)
    coin = models.IntegerField(default=0)
    last_queue_refuse = models.IntegerField(default=0)
    mmr = models.FloatField(null=True, blank=True)
    sigma = models.FloatField(null=True, blank=True)
    register_type = models.IntegerField(null=True, blank=True)
    punicao_tempo_fila = models.IntegerField(null=True, blank=True)
    tipo_tempo_punicao = models.IntegerField(null=True, blank=True)
    register_channel = models.BigIntegerField(null=True, blank=True)
    riot_verified = models.BooleanField(default=False)
    last_nick_change = models.DateTimeField(null=True, blank=True)
    ingame = models.BooleanField(default=False)
    puuid = models.CharField(max_length=100, null=True, blank=True)
    encrypted_summoner_id = models.CharField(max_length=100, null=True, blank=True)
    next_refresh = models.DateTimeField(null=True, blank=True)
    secret_queue = models.BooleanField(default=False)
    do_not_call = models.BooleanField(default=False)
    not_be_captain = models.BooleanField(default=False)
    last_game = models.DateTimeField(null=True, blank=True)
    last_alert_decay = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.inhouse_nickname