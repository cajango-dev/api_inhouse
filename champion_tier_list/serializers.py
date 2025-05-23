from rest_framework import serializers
from .models import ChampionTierList

class ChampionTierListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChampionTierList
        fields = '__all__'
