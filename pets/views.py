from django.shortcuts import render
from rest_framework import generics, permissions
from .models import PetRegister
from .serializers import PetRegisterSerializers


class ReadPets(generics.ListAPIView):
    queryset = PetRegister.objects.all()
    serializer_class = PetRegisterSerializers


class WritePets(generics.CreateAPIView):
    queryset = PetRegister.objects.all()
    serializer_class = PetRegisterSerializers
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(pet_owner_name=self.request.user)
