from django.urls import path
from .views import CreateReadPets

urlpatterns = [
    path('', CreateReadPets.as_view()),
]
