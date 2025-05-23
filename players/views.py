from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from players.models import Player
from players.serializers import PlayerDetailSerializer

class PlayerListCreate(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PlayerDetailSerializer

class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerDetailSerializer
    lookup_field = 'player_id'
    permission_classes = [IsAuthenticated]
