from rest_framework import generics
from .models import SeasonPlayerLane
from .serializers import SeasonPlayerLaneSerializer

class SeasonPlayerLaneListCreateView(generics.ListCreateAPIView):
    queryset = SeasonPlayerLane.objects.all()
    serializer_class = SeasonPlayerLaneSerializer

class SeasonPlayerLaneRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SeasonPlayerLane.objects.all()
    serializer_class = SeasonPlayerLaneSerializer
    lookup_field = 'id'
