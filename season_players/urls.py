from django.urls import path
from .views import SeasonPlayerListCreate, SeasonPlayerDetail

urlpatterns = [
    path('', SeasonPlayerListCreate.as_view(), name='season-player-list-create'),
    path('<int:pk>/', SeasonPlayerDetail.as_view(), name='season-player-detail'),
]
