from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render

# from .models import Address, Dentist, Person, Phone


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        # user = Dentist.objects.filter(username=request.user).first()
        #print(user.uf)
        return render(request, 'app/index1.html', {'user':user})

    return redirect('/login/')


# CREATE
def cadastro(request):

    if request.user.is_authenticated:
        return redirect('/home/')    

    if request.method == 'GET':
        return render(request, 'app/cadastro.html')
    
    elif request.method == 'POST':

        # Obtem o valor dos campos na requisição

        firstname = request.POST.get('firstName')
        lastnaem = request.POST.get('lastName')
        birthdate = request.POST.get('birthdate')
        emaiil = request.POST.get('email')
        cellphone = request.POST.get('cellphone')
        gender = request.POST.get('gender')
        numero_cro = request.POST.get('numero_cro')
        uf_cro = request.POST.get('uf_cro')
        numero_cnpj = request.POST.get('numero_cnpj')
        nome_legal = request.POST.get('nome_legal')
        cpf = request.POST.get('cpf')
        street_avenue = request.POST.get('street_avenue')
        house_number = request.POST.get('house_number')
        uf_residencia = request.POST.get('uf_residencia')
        additional_information = request.POST.get('additional_info')
        username = request.POST.get('username')
        password = request.POST.get('password')
        cep = request.POST.get('cep')
        city =request.POST.get('city')
 
        # Cria o usuário
        dentist = Dentist(
            username=username,
            first_name=firstname,
            last_name=lastnaem,
            email=emaiil,
            cpf = cpf,
            cnpj=numero_cnpj,
            legal_name=nome_legal,
            cro_number=numero_cro,
            uf_cro=uf_cro,
            birthdate=datetime.strptime(birthdate, '%Y-%m-%d'),
        )

        dentist.set_password(password)

        # # Cria o endereço
        # address = Address(
        #     user=dentist,
        #     cep=cep,
        #     street_avenue=street_avenue,
        #     number=house_number,
        #     city=city,
        #     uf=uf_residencia,
        #     additional_information=additional_information
        # )
        # ddd, number = cellphone[:2], cellphone[2:]
        # # Cria o telefone
        # phone = Phone(
        #     number=cellphone,
        #     ddd=ddd,
        #     user=dentist
        # )

        # # Cria o dentista
        # dentist.save()
        # address.save()
        # phone.save()


        return redirect('/login/')


# READ
def logar(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    
    if request.method =='GET':
        return render(request, 'app/login.html')
    elif request.method =='POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        
        user = authenticate(
            username=nome,
            password=senha
        )

        if user is not None:
            # login
            login(request, user)
            return redirect('/home/')
        else:
            return render(request, 'app/login.html')


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


@login_required
def sair(request):
    logout(request)
    # return HttpResponse('Deslogado')
    return redirect('/login')

