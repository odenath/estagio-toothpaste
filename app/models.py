from typing import Any
from django.contrib.auth.models import User 
from django.db import models


# # Create your models here.


class User(models.Model):

    class Meta:
        db_table = "tb_user"
    

class Person(models.Model):

    class Meta:
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

    def __repr__(self) -> str:
        return f'<Usuario {self.first_name}, {self.last_name}>'


class Dentist(User):

    class Meta:
        db_table = "tb_dentist"

    cro = models.CharField(null=False, max_length=9, unique=True)
    uf = models.CharField(null=False, max_length=2)
    cnpj = models.CharField(max_length=14)
    legal_name = models.CharField(max_length=40)
    tb_personid = models.ForeignKey(Person, on_delete=models.CASCADE) # Relacionamento 1 para muitos

    def __repr__(self) -> str:
        return f'<Dentist {self.first_name}, {self.last_name}>'


class Address(Person, models.Model):
           
    class Meta:
        db_table = "tb_address"
  
    cep = models.CharField(max_length=8, null=False)
    street_avenue = models.CharField(max_length=40, null=False)
    number = models.IntegerField(max_length=40, null=False)
    city = models.CharField(max_length=40)
    uf = models.CharField(max_length=2, null=False)
    additional_information = models.CharField(max_length=50, null=False)
    tb_personid = models.ForeignKey(Person, on_delete=models.CASCADE) # Relacionamento 1 para muitos
    
    def __repr__(self) -> str:
        return f'<Addrress {self.city}, {self.uf}>'


class Phone(models.Model):
          
    class Meta:
        db_table = "tb_phone"
                
    ddd = models.CharField(null=False, max_length=2)
    number = models.CharField(null=False, max_length=9)
    tb_personid = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __repr__(self) -> str:
        return f'<Phone {self.ddd}, {self.number}>'


class Costumer(Person, models.Model):
           
    class Meta:
        db_table = "tb_costumer"
            
    status = models.CharField(null=False, max_length=2)
    tb_personid = models.ForeignKey(Person, on_delete=models.CASCADE)

#Próximo semestre

class DentalAppointment(Dentist, Costumer, models.Model):
     
    class meta:
        db_table = "tb_dental_appointment"

    date = models.DateField(null=False)
    tb_costumerid = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    tb_dentistid = models.ForeignKey(Dentist, on_delete=models.CASCADE)

    def __repr__(self) -> str:
        return f'<DentalAppointment {self.date}, {self.tb_costumerid}>'


class Procedure(ProcedureType, Img , Tooth , DentalAppointment):
     
    class Meta:
        db_table = "tb_procedure"

    cost = models.DecimalField(null=False, max_digits=7, decimal_places=2)
    description = models.CharField(null=False, max_length=40)
    tb_procedure_typeid = models.ForeignKey(ProcedureType, on_delete=models.CASCADE)
    tb_dental_appointmentid = models.ForeignKey(DentalAppointment, on_delete=models.CASCADE)
    tb_procedure_typeid = models.ForeignKey(ProcedureType, on_delete=models.CASCADE)
    tb_toothid = models.ForeignKey(Tooth, on_delete=models.CASCADE)

    def __repr__(self) -> str:
        return f'<Procedure {self.description}, {self.cost}>'
    

class Specialty():
    
    class Meta:
        db_table = "tb_specialty"
    
    name = models.CharField(null=False, max_length=50)

    def __repr__(self) -> str:
        return f'<Specialty {self.name}>'


class ProcedureType(Specialty):
 
    class Meta:
        db_table = "tb_procedure_type"
    
    name = models.CharField(null=False, max_length=40)
    cost = models.DecimalField(null=False, max_digits=7, decimal_places=2)
    tb_specialtyid = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    
    def __repr__(self) -> str:
        return f'<ProcedureType {self.name}>'



class Tooth(Procedure):
     
    class Meta:
        db_table = "tb_tooth"

    number = models.IntegerField(null=False)
    type = models.CharField(null=False, max_length=10)


class Img(Procedure):
     
    class Meta:
        db_table = "tb_img"

    img = models.ImageField(null=False, upload_to='img')
    tb_procedureid = models.ForeignKey(Procedure, on_delete=models.CASCADE)

