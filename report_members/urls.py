from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReportMemberViewSet

router = DefaultRouter()
router.register(r'', ReportMemberViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
