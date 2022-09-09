from django.db import models
from django.contrib.auth.models import User

class PetRegister(models.Model):
    pet_name = models.CharField(max_length=50)
    pet_breed = models.CharField(max_length=50)
    pet_owner_name = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_image = models.ImageField()
    pet_birth_date = models.DateField()
    pet_register_date = models.DateTimeField(auto_now_add=True)