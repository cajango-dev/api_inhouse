from rest_framework import viewsets
from .models import ReportMember
from .serializers import ReportMemberSerializer

class ReportMemberViewSet(viewsets.ModelViewSet):
    queryset = ReportMember.objects.all()
    serializer_class = ReportMemberSerializer
