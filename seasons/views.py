from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from seasons.models import Season
from seasons.serializers import SeasonDetailSerializer

class SeasonListCreate(generics.ListCreateAPIView):
    queryset = Season.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = SeasonDetailSerializer

class SeasonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonDetailSerializer
    lookup_field = 'season'
    permission_classes = [IsAuthenticated]
