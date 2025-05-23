from django.urls import path
from .views import StaffListCreateAPIView, StaffRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('staff/', StaffListCreateAPIView.as_view(), name='staff-list-create'),
    path('staff/<int:pk>/', StaffRetrieveUpdateDestroyAPIView.as_view(), name='staff-detail'),
]
