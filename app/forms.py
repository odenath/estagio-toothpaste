from datetime import datetime

from django import forms
from django.core.exceptions import ValidationError


class PersonForm(forms.Form):

    GENDER_CHOICES = [
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('O', 'OTHER')
    ]

    first_name = forms.CharField(max_length=40, label="First Name")
    last_name = forms.CharField(max_length=40, label="Last Name")
    birth_date = forms.DateField(label="Birth Date")
    cpf = forms.CharField(max_length=11, label="CPF")
    email = forms.EmailField(max_length=50, label="Email")
    gender = forms.ChoiceField(choices=GENDER_CHOICES)

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if len(first_name) < 3:
            raise ValidationError("O Nome deve ter pelo menos 3 caracteres")
        return first_name 

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if len(last_name) < 3:
            raise ValidationError("O Sobre Nome deve ter pelo menos 3 caracteres")
        return last_name

    def clean_birth_date(self):
        birth_date = self.cleaned_data['birth_date']
        # Convert 
        # if birth_date > datetime.today():
        #     raise ValidationError("Birth Date must be in the past")
        return birth_date

    def clean_cpf(self):
        # TODO: Validate CPF
        cpf = self.cleaned_data['cpf']

        if len(cpf) != 11 or not cpf.isdigit():
            raise ValidationError("O CPF precisa ter 11 digitos e apenas numeros")

        return cpf

class AddressForm(forms.Form):

    cep = forms.CharField(max_length=8, label="CEP")
    street_avenue = forms.CharField(max_length=40, label="Street/Avenue")
    number = forms.IntegerField(label="Number")
    city = forms.CharField(max_length=40, label="City")
    uf = forms.CharField(max_length=2, label="UF")
    additional_information = forms.CharField(max_length=50, label="Additional Information")

    def clean_cep(self):
        #! TODO:Validate CEP
        cep = self.cleaned_data['cep']
        if len(cep) != 8 or not cep.isdigit():
            raise ValidationError("O CEP precisa ter 8 digitos e apenas numeros")

        return cep
    

class PhoneForm(forms.Form):

    phone = forms.CharField(max_length=11, label="Phone")

    def clean_phone(self):

        phone = self.cleaned_data['phone']
        if len(phone) != 11 or not phone.isdigit():
            raise ValidationError("O telefone precisa ter 11 digitos e apenas numeros")

        return phone

class CostumerForm(forms.Form):
    
    # O campo status é opcional
    status = forms.BooleanField(required=False, label="Active")


class DentistForm(forms.Form):
    
    cro = forms.CharField(max_length=9, label="CRO")
    uf_cro = forms.CharField(max_length=2, label="UF CRO")
    cnpj = forms.CharField(max_length=9, label="CNPJ", required=False)
    legal_name = forms.CharField(max_length=40, label="Legal Name", required=False)





#https://pypi.org/project/django-cpf/
