from django.db import models

class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    discord_id = models.BigIntegerField(unique=True)
    discord_user = models.CharField(max_length=255, unique=True)
    added_by = models.BigIntegerField(null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.discord_user
