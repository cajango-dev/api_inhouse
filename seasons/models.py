from django.db import models

# Modelo SEASON
class Season(models.Model):
    season = models.AutoField(primary_key=True)
    status = models.BooleanField(default=False)
    season_in_time = models.IntegerField(null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    pause = models.DateTimeField(null=True, blank=True)
    on_off = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Season {self.season}"
