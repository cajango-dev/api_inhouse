from django.urls import path
from .views import ChampionTierListListCreate, ChampionTierListRetrieveUpdateDestroy

urlpatterns = [
    path('', ChampionTierListListCreate.as_view(), name='champion_tier_list_list_create'),
    path('<int:pk>/', ChampionTierListRetrieveUpdateDestroy.as_view(), name='champion_tier_list_detail'),
]
