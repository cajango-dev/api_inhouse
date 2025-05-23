from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('players/', include('players.urls')),
    path('seasons/', include('seasons.urls')),
    path('season_players/', include('season_players.urls')),
    path('player_matches/', include('player_matches.urls')),
    path('matches/', include('matches.urls')),
    path('season-player-lanes/', include('season_player_lanes.urls')),
    path('champions/', include('champions.urls')),
    path('staff/', include('staff.urls')),
    path('champion-tier-list/', include('champion_tier_list.urls')),
    path('inqueue/', include('inqueue.urls')),

    path('auth/', include('authentication.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

