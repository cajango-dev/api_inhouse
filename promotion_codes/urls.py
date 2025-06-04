from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PromotionCodeViewSet

router = DefaultRouter()
router.register(r'', PromotionCodeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]