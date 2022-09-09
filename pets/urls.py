from django.urls import path
from .views import ReadPets, WritePets
urlpatterns = [
    path('/read', ReadPets.as_view()),
    path('/write', WritePets.as_view()),
]
