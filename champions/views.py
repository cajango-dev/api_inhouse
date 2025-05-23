from rest_framework import generics
from .models import Champion
from .serializers import ChampionSerializer

class ChampionListCreateView(generics.ListCreateAPIView):
    queryset = Champion.objects.all()
    serializer_class = ChampionSerializer

class ChampionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Champion.objects.all()
    serializer_class = ChampionSerializer
    lookup_field = 'id'
