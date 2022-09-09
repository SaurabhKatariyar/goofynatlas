from django.shortcuts import render
from rest_framework import generics
from .models import PetRegister
from .serializers import PetRegisterSerializers


class CreateReadPets(generics.ListCreateAPIView):
    queryset = PetRegister.objects.all()
    serializer_class = PetRegisterSerializers
