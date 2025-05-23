from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from season_players.models import SeasonPlayer
from season_players.serializers import SeasonPlayerDetailSerializer

class SeasonPlayerListCreate(generics.ListCreateAPIView):
    queryset = SeasonPlayer.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = SeasonPlayerDetailSerializer

class SeasonPlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SeasonPlayer.objects.all()
    serializer_class = SeasonPlayerDetailSerializer
    permission_classes = [IsAuthenticated]
