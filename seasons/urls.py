from django.urls import path
from .views import SeasonListCreate, SeasonDetail

urlpatterns = [
    path('', SeasonListCreate.as_view(), name='season-list-create'),
    path('<str:season>/', SeasonDetail.as_view(), name='season-detail'),
]
