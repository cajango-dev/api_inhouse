from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.conf import settings
import jwt
import datetime

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

