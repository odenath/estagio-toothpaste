from typing import Any
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Usuario(User, models.Model):
    __tablename__ = 'usuario'    
    uf = models.CharField(max_length=2)

    def __str__(self) -> str:
        return self.username
    
