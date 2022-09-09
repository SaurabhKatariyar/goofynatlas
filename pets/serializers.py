from rest_framework import serializers
from .models import PetRegister

class PetRegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = PetRegister
        fields = ['id', 'pet_name', 'pet_breed', 'pet_owner_name', 'pet_image',
                  'pet_birth_date', 'pet_register_date']


