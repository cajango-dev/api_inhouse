from django.db import models

class Reason(models.Model):
    description = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.description
