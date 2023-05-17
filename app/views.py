from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        user = Usuario.objects.filter(username=request.user).first()
        print(user.uf)
        return render(request, 'app/index1.html', {'user':user})

    return redirect('/login/')


# CREATE
def cadastro(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    
    if request.method == 'GET':
        return render(request, 'app/cadastro.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        
        # user = User.objects.create_user(
        #     username=nome,
        #     password=senha
        # )

        user = Usuario.objects.create_user(
            username=nome,
            password=senha,
            uf="MG"
        )

        user.save()

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

