from django.urls import path
from .views import SeasonPlayerLaneListCreateView, SeasonPlayerLaneRetrieveUpdateDestroyView

urlpatterns = [
    path('', SeasonPlayerLaneListCreateView.as_view(), name='season-player-lane-list-create'),
    path('<int:id>/', SeasonPlayerLaneRetrieveUpdateDestroyView.as_view(), name='season-player-lane-detail'),
]
