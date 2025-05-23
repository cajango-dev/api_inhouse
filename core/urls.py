from django.urls import path, include
from core import views as core_views

urlpatterns = [
    # Endpoints auxiliares globais
    path('generate-token/', core_views.generate_test_token, name='generate_test_token'),
    path('matches/queue/<str:queue>/', core_views.matches_by_queue, name='matches_by_queue'),

    # Apps
    path('players/', include('players.urls')),
    path('matches/', include('matches.urls')),
    path('seasons/', include('seasons.urls')),
    path('season-players/', include('seasonplayers.urls')),
    path('player-matches/', include('playermatches.urls')),
    path('auth/', include('authentication.urls')),
]
