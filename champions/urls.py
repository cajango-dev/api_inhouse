from django.urls import path
from .views import ChampionListCreateView, ChampionRetrieveUpdateDestroyView

urlpatterns = [
    path('', ChampionListCreateView.as_view(), name='champion-list-create'),
    path('<int:id>/', ChampionRetrieveUpdateDestroyView.as_view(), name='champion-detail'),
]
