from django.urls import path
from .views import (
    PlayerMatchListCreate,
    PlayerMatchDetail,
    LastMatchesByPlayer,
)

urlpatterns = [
    path('', PlayerMatchListCreate.as_view(), name='player-match-list-create'),
    path('last-matches/<str:identifier>/', LastMatchesByPlayer.as_view(), name='last-matches-by-player'),
    path('<str:player_id>/<str:match_id>/', PlayerMatchDetail.as_view(), name='player-match-detail'),
]
