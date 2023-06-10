from typing import Any

from django.contrib.auth.models import User
from django.db import models

import datetime

# # Create your models here.


class Person(models.Model):

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"
        db_table = "tb_person"

        
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other")
    ]

    first_name = models.CharField(max_length=40, null=False)
    last_name = models.CharField(max_length=40, null=False)
    birth_date = models.DateField(null=False)
    cpf = models.CharField(max_length=11, null=False, unique=True)
    email = models.EmailField(null=False, unique=True, max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __repr__(self) -> str:
        return f'<Usuario {self.first_name}, {self.last_name}>'

    def get_full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def get_birth_date(self) -> str:
        return self.birth_date.strftime("%Y-%m-%d")
    
    def update_fields(self, **kwargs) -> None:

        for key, value in kwargs.items():
            if hasattr(self, key) and key != "id":
                setattr(self, key, value)
        self.save()
    
    

class Address(models.Model):
           
    class Meta:
       
        verbose_name = "Address"
        verbose_name_plural = "Addresses"
        db_table = "tb_address"
  
    cep = models.CharField(max_length=8, null=False)
    street_avenue = models.CharField(max_length=40, null=False)
    number = models.IntegerField(null=False)
    city = models.CharField(max_length=40)
    uf = models.CharField(max_length=2, null=False)
    additional_information = models.CharField(max_length=50, null=False)
    tb_person = models.OneToOneField(Person, on_delete=models.CASCADE, unique=True)
    
    def __repr__(self) -> str:
        return f'<Addrress {self.city}, {self.uf}>'

    def update_fields(self, **kwargs) -> None:

        for key, value in kwargs.items():
            if hasattr(self, key) and key != "id":
                setattr(self, key, value)
        self.save()

class Phone(models.Model):
          
    class Meta:

        verbose_name = "Phone"
        verbose_name_plural = "Phones"
        db_table = "tb_phone"
                
    ddd = models.CharField(null=False, max_length=2)
    number = models.CharField(null=False, max_length=9)
    tb_person = models.ForeignKey(Person, on_delete=models.CASCADE)


    def __repr__(self) -> str:
        return f'<Phone {self.ddd}, {self.number}>'

    def update_fields(self, **kwargs) -> None:
        for key, value in kwargs.items():
            if hasattr(self, key) and key != "id":
                setattr(self, key, value)
        self.save()
    
class Dentist(models.Model):

    class Meta:
        verbose_name = "Dentist"
        verbose_name_plural = "Dentists"
        db_table = "tb_dentist"

    cro = models.CharField(null=False, max_length=9, unique=True)
    uf_cro = models.CharField(null=False, max_length=2)
    cnpj = models.CharField(max_length=14)
    legal_name = models.CharField(max_length=40)
    tb_person = models.OneToOneField(Person, on_delete=models.CASCADE, unique=True) # Relacionamento 1 para 1

    def __repr__(self) -> str:
        return f'<Dentist {self.cro}, {self.uf}>'

    def get_full_name(self) -> str:
        return self.tb_person.get_full_name()

    def update_fields(self, **kwargs) -> None:

        for key, value in kwargs.items():
            if hasattr(self, key) and key != "id":
                setattr(self, key, value)
        self.save()
    
    
class Costumer(models.Model):
           
    class Meta:
        verbose_name = "Costumer"
        verbose_name_plural = "Costumers"
        db_table = "tb_costumer"
            
    status = models.BooleanField(null=False, default=True)
    tb_person = models.ForeignKey(Person, on_delete=models.CASCADE) 

    def update_fields(self, **kwargs) -> None:

        for key, value in kwargs.items():
            if hasattr(self, key) and key != "id":
                setattr(self, key, value)
        self.save()
    
    def update_status(self) -> bool:
        """
        Iremos trocar o status de ativo para inativo depois de 1 ano de inatividade
        Por hora, iremos considerar o tempo de atividade como a data de cadastro, pois não temos os dados de atendimento implementados.
        """

        today = datetime.datetime.now().date()
        created_date = self.tb_person.created_date.date()
        
        if (today - created_date).days > 365:
            self.status = False
            self.save()
            return False
        return True

#Próximo semestre

# class DentalAppointment(Dentist, Costumer, models.Model):
     
#     class meta:
#         db_table = "tb_dental_appointment"

#     date = models.DateField(null=False)
#     tb_costumerid = models.ForeignKey(Costumer, on_delete=models.CASCADE)
#     tb_dentistid = models.ForeignKey(Dentist, on_delete=models.CASCADE)

#     def __repr__(self) -> str:
#         return f'<DentalAppointment {self.date}, {self.tb_costumerid}>'



# class Specialty():
    
#     class Meta:
#         db_table = "tb_specialty"
    
#     name = models.CharField(null=False, max_length=50)

#     def __repr__(self) -> str:
#         return f'<Specialty {self.name}>'


# class ProcedureType(models.Model):
 
#     class Meta:
#         db_table = "tb_procedure_type"
    
#     name = models.CharField(null=False, max_length=40)
#     cost = models.DecimalField(null=False, max_digits=7, decimal_places=2)
#     tb_specialtyid = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    
#     def __repr__(self) -> str:
#         return f'<ProcedureType {self.name}>'


# class Tooth(models.Model):
     
#     class Meta:
#         db_table = "tb_tooth"

#     number = models.IntegerField(null=False)
#     type = models.CharField(null=False, max_length=10)




# class Procedure(models.Model):
     
#     class Meta:
#         db_table = "tb_procedure"

#     cost = models.DecimalField(null=False, max_digits=7, decimal_places=2)
#     description = models.CharField(null=False, max_length=40)
#     tb_procedure_typeid = models.ForeignKey(ProcedureType, on_delete=models.CASCADE)
#     tb_dental_appointmentid = models.ForeignKey(DentalAppointment, on_delete=models.CASCADE)
#     tb_procedure_typeid = models.ForeignKey(ProcedureType, on_delete=models.CASCADE)
#     tb_toothid = models.ForeignKey(Tooth, on_delete=models.CASCADE)

#     def __repr__(self) -> str:
#         return f'<Procedure {self.description}, {self.cost}>'
    
# class Img(models.Model):
     
#     class Meta:
#         db_table = "tb_img"

#     img = models.ImageField(null=False, upload_to='img')
#     tb_procedureid = models.ForeignKey(Procedure, on_delete=models.CASCADE)
