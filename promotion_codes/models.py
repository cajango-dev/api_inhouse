from django.db import models

class PromotionCode(models.Model):
    tier = models.IntegerField()
    code = models.CharField(max_length=100, unique=True)
    redeem_until = models.IntegerField()
    vip_days = models.IntegerField()
    created_by = models.IntegerField()
    redeemed = models.BooleanField(default=False)
    type_vip = models.IntegerField()

    def __str__(self):
        return self.code

