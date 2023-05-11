#  from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return render(request, 'app/index.html')
    else:
        return render(request, 'app/login.html')


def login(request):
    return render(request, 'app/login.html')


def cadastro(request):
    print('posso fazer uma coisa ')
    return HttpResponse('app/cadastro')


def exemplo(request):
    print('posso fazer alguma coisa')
    return HttpResponse('exemplo')
