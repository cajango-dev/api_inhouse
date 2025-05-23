from django.urls import path
from .views import PlayerListCreate, PlayerDetail

urlpatterns = [
    path('', PlayerListCreate.as_view(), name='player-list-create'),
    path('<str:player_id>/', PlayerDetail.as_view(), name='player-detail'),
]
