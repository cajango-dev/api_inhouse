from rest_framework import serializers
from .models import PromotionCode

class PromotionCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromotionCode
        fields = '__all__'
