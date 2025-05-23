from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, APIView
from .models import Match
from .serializers import MatchDetailSerializer, MatchListSerializer, MatchListWithPlayersSerializer


class MatchQueueBySeasonView(APIView):
    def get(self, request, queue_id, season_id):
        quantidade = request.query_params.get('quantidade')
        
        try:
            quantidade = int(quantidade) if quantidade else 10
        except ValueError:
            return Response({"error": "Quantidade inválida."}, status=status.HTTP_400_BAD_REQUEST)

        matches = Match.objects.filter(queue=queue_id, season=season_id).order_by('-start_time')[:quantidade]

        serializer = MatchListSerializer(matches, many=True)

        # Transforma a lista de matches serializados em dicionário com chave match_id
        response_data = {}
        for match_data in serializer.data:
            match_id = match_data.get('match_id')
            if match_id:
                response_data[match_id] = match_data

        return Response(response_data, status=status.HTTP_200_OK)


class MatchListView(APIView):
    def get(self, request):
        matches = Match.objects.all()
        serializer = MatchListSerializer(matches, many=True)  # corrigido para MatchListSerializer
        return Response(serializer.data)


class MatchDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchDetailSerializer  # corrigido para MatchDetailSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def matches_by_queue(request, queue):
    quantidade = request.query_params.get('quantidade', None)
    matches = Match.objects.filter(queue=queue).select_related('season').order_by('-start_time')

    if quantidade:
        try:
            matches = matches[:int(quantidade)]
        except ValueError:
            return Response({"detail": "Parâmetro 'quantidade' inválido."}, status=status.HTTP_400_BAD_REQUEST)

    serializer = MatchListWithPlayersSerializer(matches, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def matches_list(request):
    matches = Match.objects.all().select_related('season').order_by('-start_time')
    serializer = MatchListWithPlayersSerializer(matches, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class MatchListCreate(generics.ListCreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchDetailSerializer
    permission_classes = [IsAuthenticated]


class MatchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchDetailSerializer
    lookup_field = 'match_id'
    permission_classes = [IsAuthenticated]
