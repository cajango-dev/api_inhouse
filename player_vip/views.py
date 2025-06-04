from rest_framework import viewsets
from .models import PlayerVIP
from .serializers import PlayerVIPSerializer

class PlayerVIPSerializer(viewsets.ModelViewSet):
    queryset = PlayerVIP.objects.all()
    serializer_class = PlayerVIPSerializer
