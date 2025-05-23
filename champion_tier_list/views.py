from rest_framework import generics
from .models import ChampionTierList
from .serializers import ChampionTierListSerializer

class ChampionTierListListCreate(generics.ListCreateAPIView):
    queryset = ChampionTierList.objects.all()
    serializer_class = ChampionTierListSerializer

class ChampionTierListRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChampionTierList.objects.all()
    serializer_class = ChampionTierListSerializer
