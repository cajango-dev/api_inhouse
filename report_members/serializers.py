from rest_framework import serializers
from .models import ReportMember

class ReportMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportMember
        fields = '__all__'
