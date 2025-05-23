from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from player_matches.models import PlayerMatch
from player_matches.serializers import PlayerMatchDetailSerializer
from matches.views import MatchListView
from players.models import Player
from matches.models import Match
from matches.serializers import MatchListWithPlayersSerializer

class PlayerMatchListCreate(generics.ListCreateAPIView):
    queryset = PlayerMatch.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PlayerMatchDetailSerializer

class PlayerMatchDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlayerMatchDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        player_id = self.kwargs.get("player_id")
        match_id = self.kwargs.get("match_id")
        try:
            return PlayerMatch.objects.get(player_id=player_id, match_id=match_id)
        except PlayerMatch.DoesNotExist:
            raise NotFound("PlayerMatch com essas chaves não foi encontrado.")

class LastMatchesByPlayer(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, identifier):
        player = Player.objects.filter(player_id=identifier).first()
        if not player:
            player = Player.objects.filter(discord_id=identifier).first()

        if not player:
            return Response({"detail": "Player não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        player_matches = PlayerMatch.objects.filter(player=player)\
            .select_related('match')\
            .order_by('-match__start_time')[:10]

        match_ids = [pm.match.match_id for pm in player_matches]
        matches = Match.objects.filter(match_id__in=match_ids).select_related('season')

        serializer = MatchListWithPlayersSerializer(matches, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
