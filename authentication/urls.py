from django.urls import path
from .views import generate_test_token

urlpatterns = [
    path('generate-token/', generate_test_token, name='generate-test-token'),
]
