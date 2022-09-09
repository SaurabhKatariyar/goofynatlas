from django.shortcuts import render
from rest_framework import generics
from .models import PetRegister
from .serializers import PetRegisterSerializers


class ReadPets(generics.ListAPIView):
    queryset = PetRegister.objects.all()
    serializer_class = PetRegisterSerializers


class WritePets(generics.CreateAPIView):
    queryset = PetRegister.objects.all()
    serializer_class = PetRegisterSerializers
