from rest_framework import serializers
from .models import InQueue

class InQueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = InQueue
        fields = '__all__'
