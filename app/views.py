from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

from app.forms import AddressForm, CostumerForm, PersonForm, PhoneForm, DentistForm, UserForm
from app.models import Address, Costumer, Dentist, Person, Phone
from app_customauth.models import CustomUser as User


# Create your views here.
def home(request):

    if request.user.is_authenticated:
        user = Dentist.objects.filter(customuser=request.user.pk).first()

        return render(request, 'app/index.html', {'user':user})

    return redirect('/login/')


# CREATE

def cadastro(request):

    errors = []
    if request.user.is_authenticated:
        return redirect('/home/')


    elif request.method == 'POST':

        errors = []
        person_form = PersonForm(request.POST) 
        address_form = AddressForm(request.POST)
        phone_form = PhoneForm(request.POST)
        user_form = UserForm(request.POST)
        dentist_form = DentistForm(request.POST)
        #import pdb; pdb.set_trace()
        if person_form.is_valid() and address_form.is_valid() and phone_form.is_valid() and user_form.is_valid() and dentist_form.is_valid():

            # checa se existe algum usuário com o mesmo login
            if User.objects.filter(login=user_form.cleaned_data['login']).exists():
                errors.append('Usuário já cadastrado')
                return render(request, 'app/cadastro.html', {'errors':errors})

            # checa se existe algum usuário com o mesmo cpf
            if Person.objects.filter(cpf=person_form.cleaned_data['cpf']).exists():
                errors.append('CPF já cadastrado')
                return render(request, 'app/cadastro.html', {'errors':errors})
            
            # checa se existe algum usuário com o mesmo email
            if Person.objects.filter(email=person_form.cleaned_data['email']).exists():

                errors.append('Email já cadastrado')
                return render(request, 'app/cadastro.html', {'errors':errors})
            
            # checa se exsite alguum dentista com o mesmo cro
            # como o CRO não é obrigatório, é necessário checar se ele existe
            try:
                if Dentist.objects.filter(cro=dentist_form.cleaned_data['cro']).exists():
                    errors.append('CRO já cadastrado')
                    return render(request, 'app/cadastro.html', {'errors':errors})
            except KeyError:
                dentist_form.cleaned_data['cro'] = None

            if Person.objects.filter(cpf=person_form.cleaned_data['cpf']).exists():
                errors.append('CPF já cadastrado')
                return render(request, 'app/cadastro.html', {'errors':errors})

            
            person = Person(**person_form.clean())
            address = Address(**address_form.clean(), tb_person=person)
            dentist = Dentist(**dentist_form.clean(), tb_person=person)
            user = User(**user_form.clean(), tb_dentist=dentist)

            user.set_password(user_form.cleaned_data['password'])

            ddd = phone_form.cleaned_data['phone'][:2]
            number = phone_form.cleaned_data['phone'][2:]

            phone = Phone(ddd=ddd, number=number, tb_person=person)

            person.save()
            address.save()
            phone.save()
            dentist.save()
            user.save()

            return redirect('/login/')
        else:

            errors.append(person_form.errors.values())
            errors.append(address_form.errors.values())
            errors.append(phone_form.errors.values())
            errors.append(user_form.errors.values())
            errors.append(dentist_form.errors.values())

            errors = [item for sublist in errors for item in sublist]
    return render(request, 'app/auth/cadastro.html', {'errors': errors})

# READ
def logar(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    
    if request.method =='GET':
        return render(request, 'app/auth/login.html')
    elif request.method =='POST':

        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        
        user = authenticate(
            login=nome,
            password=senha
        )

        if user is not None:
            # login
            login(request, user)
            return redirect('/home/')
        else:
            return render(request, 'app/auth/login.html')


# UPDATE
@login_required
def update_pass(request):
    novonome = request.POST.get('nome')
    novasenha = request.POST.get('senha')
    user = User.objects.filter(username=request.user).first()
    if novasenha:
        user.username = novonome
        user.set_password(novasenha)
        user.save()
        logout(request)
        # return HttpResponse("Senha alterada com sucesso")
        return redirect('/login')


# DELETE
@login_required
def delete_user(request):
    user = User.objects.filter(username=request.user).first()
    user.delete()
    
    # return HttpResponse("Usuario deletado")
    return redirect('/login/')

def recovery_password(request):

    return render(request, 'app/auth/recovery-password.html')

@login_required
def sair(request):
    logout(request)
    # return HttpResponse('Deslogado')
    return redirect('/login')

@login_required
def create_costumer(request):

    errors = []
    if request.method == "POST":
        
        person_form = PersonForm(request.POST) 
        address_form = AddressForm(request.POST)
        costumer_form = CostumerForm(request.POST)
        phone_form = PhoneForm(request.POST)

        if (person_form.is_valid() and address_form.is_valid() and costumer_form.is_valid() and phone_form.is_valid()):
            
            p = Person.objects.filter(cpf=person_form.cleaned_data['cpf']).first()
            if p:
                return render(request, 'app/cadastro-cliente.html', {'errors': ['CPF já cadastrado']})

            p = Person.objects.filter(email=person_form.cleaned_data['email']).first()
            if p:
                return render(request, 'app/cadastro-cliente.html', {'error': ['Email já cadastrado']})

            person = Person(**person_form.clean())
            address = Address(**address_form.clean(), tb_person=person)
            costumer = Costumer(**costumer_form.clean(), tb_person=person)
            costumer.status = True
            
            ddd = phone_form.cleaned_data['phone'][:2]
            number = phone_form.cleaned_data['phone'][2:]

            phone = Phone(ddd=ddd, number=number, tb_person=person)

            person.save()
            address.save()
            costumer.save()
            phone.save()

            return redirect('/vizualize-costumer/')

        # Caso o formulário não seja válido, vamos retornar o problema
        else:
            errors.append(person_form.errors.values())
            errors.append(address_form.errors.values())
            errors.append(costumer_form.errors.values())
            errors.append(phone_form.errors.values())
            errors = [item for sublist in errors for item in sublist]
            return render(request, 'app/cadastro-cliente.html', {'errors': errors})
    return render(request, 'app/cadastro-cliente.html')

@login_required
def list_costumer(request):

    costumers = Costumer.objects.all()
    # Vamos atualizar o status do cliente
    for costumer in costumers:
        costumer.update_status()

    return render(request, 'app/listar-clientes.html', {'costumers': costumers})

@login_required
def delete_costumer(request, id):
    
    costumer = Costumer.objects.filter(id=id).first()
    # Get the person
    if costumer:
        person = costumer.tb_person
        person.delete()
    
    return redirect('/vizualize-costumer/')


@login_required
def update_costumer(request, id):
    
    costumer = Costumer.objects.filter(id=id).first()
    errors = []
    # Get costumer phone
    phone = costumer.tb_person.phone_set.first()
    if not costumer:
        return redirect('/vizualize-costumer/')
    
    if request.method == "POST":
        
        person_form = PersonForm(request.POST) 
        address_form = AddressForm(request.POST)
        costumer_form = CostumerForm(request.POST)
        phone_form = PhoneForm(request.POST)

        if (person_form.is_valid() and address_form.is_valid() and costumer_form.is_valid() and phone_form.is_valid()):

            costumer.tb_person.update_fields(**person_form.clean())
            costumer.tb_person.address.update_fields(**address_form.clean())
            costumer.update_fields(**costumer_form.clean())
            costumer.tb_person.phone_set.first().update_fields(**phone_form.clean())
            costumer.update_fields(**costumer_form.clean())
            return redirect('/vizualize-costumer/')
        else:
            #import pdb; pdb.set_trace()
            errors.append(person_form.errors.values())
            errors.append(address_form.errors.values())
            errors.append(costumer_form.errors.values())
            errors = [item for sublist in errors for item in sublist]
        
    return render(
        request,
          'app/editar-cliente.html',
            {'costumer': costumer, 'phone': phone, 'F': 'F', 'M': 'M', 'O': 'O', 'birth_date': costumer.tb_person.get_birth_date(), 'errors': errors}
            )

