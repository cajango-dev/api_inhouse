from django.db import models

class Report(models.Model):
    discord_id = models.BigIntegerField()
    reason_text = models.TextField()

    def __str__(self):
        return f"Report {self.id} - Discord ID: {self.discord_id}"