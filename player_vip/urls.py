from rest_framework.routers import DefaultRouter
from .views import PlayerVIPViewSet

router = DefaultRouter()
router.register(r'player-vips', PlayerVIPViewSet)

urlpatterns = router.urls