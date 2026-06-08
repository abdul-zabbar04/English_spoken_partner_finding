from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

class User(AbstractUser):
    username= None
    email = models.EmailField(
        unique=True, db_index=True,
        max_length=255
    )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects= CustomUserManager()
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS= []

    class Meta:
        db_table = 'users'
        ordering= ['-created_at']

    def __str__(self):
        return self.email