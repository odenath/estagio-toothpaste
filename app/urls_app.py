from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name='home'),
    path("login/", views.logar, name='login'),
    path("cadastro/", views.cadastro, name='cadastro'),
    path("updatepass/", views.update_pass, name='updatepass'),
    path("delete/", views.delete_user, name='delete'),
    path("logout/", views.sair, name='logout'),
]
