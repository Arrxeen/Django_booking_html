from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name}, {self.last_login}, {self.username}"
    
