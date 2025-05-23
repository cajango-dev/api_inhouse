from django.urls import path
from .views import MatchQueueBySeasonView, MatchListCreate, MatchDetail, matches_by_queue, matches_list

urlpatterns = [
    path('fila/<int:queue_id>/season/<int:season_id>/', MatchQueueBySeasonView.as_view(), name='match-queue-by-season'),
    path('by-queue/<str:queue>/', matches_by_queue, name='matches-by-queue'),
    path('all/', matches_list, name='matches-list'),
    path('<str:match_id>/', MatchDetail.as_view(), name='match-detail'),
    path('', MatchListCreate.as_view(), name='match-list-create'),
]
