from typing import Any

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Person(User, models.Model):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other")
    ]
    __tablename__ = 'tb_user'
    birthdate = models.DateTimeField(null=False)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default="M"
    )
    cpf = models.CharField(max_length=11)

    def __repr__(self) -> str:
        return f'<Usuario {self.first_name}, {self.last_name}>'


class Dentist(Person, models.Model):
    __tablename__ = "tb_dentist"
    cro_number = models.CharField(null=False, max_length=8)
    uf_cro = models.CharField(null=False, max_length=2)
    cnpj = models.CharField(max_length=14, null=False)
    legal_name = models.CharField(max_length=40, null=False)


class Address(models.Model):
    __tablename__ = "tp_address"
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    cep = models.CharField(max_length=8, null=False)
    street_avenue = models.CharField(max_length=40, null=False)
    number = models.IntegerField(null=False)
    city = models.CharField(max_length=40, null=False)
    uf = models.CharField(max_length=2, null=False)
    additional_information = models.CharField(max_length=50, null=False)

    def __repr__(self) -> str:
        return f'<Addrress {self.city}, {self.uf}>'


class Phone(models.Model):
    __tablename__ = "tb_phone"
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    ddd = models.CharField(null=False, max_length=2)
    number = models.CharField(null=False, max_length=9)

    def __repr__(self) -> str:
        return f"<Phone ({self.ddd}){self.number}>"
