from rest_framework import viewsets
from .models import InQueue
from .serializers import InQueueSerializer

class InQueueViewSet(viewsets.ModelViewSet):
    queryset = InQueue.objects.all()
    serializer_class = InQueueSerializer
