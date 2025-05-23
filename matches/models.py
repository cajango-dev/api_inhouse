from django.db import models
from seasons.models import Season

# Modelos MATCH (Partida)
class Match(models.Model):
    match_id = models.CharField(max_length=255)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    status = models.BooleanField(default=False)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)

    winner = models.IntegerField(null=True, blank=True)
    mmr_blue = models.IntegerField(null=True, blank=True)
    mmr_red = models.IntegerField(null=True, blank=True)

    blue_captain = models.IntegerField(null=True, blank=True)
    red_captain = models.IntegerField(null=True, blank=True)
    match_found_id = models.IntegerField(null=True, blank=True)
    category_id = models.IntegerField(null=True, blank=True)
    thread_log_id = models.IntegerField(null=True, blank=True)
    queue = models.IntegerField(null=True, blank=True)
    staff_calls = models.IntegerField(null=True, blank=True)
    history_msg = models.IntegerField(null=True, blank=True)

    draftlol_room = models.TextField(null=True, blank=True)
    draftlol_password = models.TextField(null=True, blank=True)
    draftlol_start = models.TextField(null=True, blank=True)

    webhook_lobby = models.TextField(null=True, blank=True)
    webhook_blue = models.TextField(null=True, blank=True)
    webhook_red = models.TextField(null=True, blank=True)

    draft_ended = models.BooleanField(default=False)

    def __str__(self):
        return self.match_id

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['match_id', 'season'], name='unique_match_per_season')
        ]
