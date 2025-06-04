from django.db import models
from players.models import Player
from report.models import Report

class ReportMember(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return f"Report {self.report.id} - Player {self.player.player_id}"
