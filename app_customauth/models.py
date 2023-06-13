from typing import Any, Optional, Union

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

from app.models import Dentist

# Create your models here.

class CustomUserManager(BaseUserManager):

    def create_user(self, tb_dentist: Dentist, login=None, password=None ) -> Any:
    
        dentist = Dentist.objects.get(id=tb_dentist.id)
        user = self.model(
            tb_Dentist=dentist,
            login=login,

        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, tb_dentist: Dentist, login=None, password=None) -> Any:

        user = self.create_user(
            tb_Dentist=tb_dentist,
            login=login,
            password=password
        )

        user.is_admin = True
        user.save(using=self._db)
        return user

    
class CustomUser(AbstractBaseUser):

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "tb_user"

    
    
    tb_dentist = models.OneToOneField(Dentist, on_delete=models.CASCADE, unique=True)
    login = models.CharField(max_length=40, null=False, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=255, null=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False) 
    last_access_date = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "login"
    REQUIRED_FIELDS = ["tb_dentist"]

    def __repr__(self) -> str:
        return self.tb_dentist.get_full_name()
