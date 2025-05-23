from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InQueueViewSet

router = DefaultRouter()
router.register(r'inqueue', InQueueViewSet, basename='inqueue')

urlpatterns = [
    path('', include(router.urls)),
]
