from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import datetime
import jwt

from matches.models import Match
from matches.serializers import MatchListWithPlayersSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def generate_test_token(request):
    payload = {
        "user_id": 1,
        "username": "testuser",
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=7)
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    return Response({"token": token})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def matches_by_queue(request, queue):
    quantidade = request.query_params.get('quantidade', None)
    matches = Match.objects.filter(queue=queue).select_related('season').order_by('-start_time')

    if quantidade:
        try:
            quantidade = int(quantidade)
            matches = matches[:quantidade]
        except ValueError:
            return Response({"detail": "Parâmetro 'quantidade' inválido."}, status=status.HTTP_400_BAD_REQUEST)

    serializer = MatchListWithPlayersSerializer(matches, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
