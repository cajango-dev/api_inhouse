from rest_framework import viewsets
from .models import PromotionCode
from .serializers import PromotionCodeSerializer

class PromotionCodeViewSet(viewsets.ModelViewSet):
    queryset = PromotionCode.objects.all()
    serializer_class = PromotionCodeSerializer
