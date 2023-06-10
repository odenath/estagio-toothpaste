from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name='home'),
    path("login/", views.logar, name='login'),
    path("cadastro/", views.cadastro, name='cadastro'),
    path("updatepass/", views.update_pass, name='updatepass'),
    path("delete/", views.delete_user, name='delete'),
    path("logout/", views.sair, name='logout'),
    #daqui para baixo troquei:
    path("create-costumer/", views.create_costumer, name="create_costumer"),
    path("vizualize-costumer/", views.list_costumer, name="vizualize_costumer"),
    path('delete-cliente/<int:id>/', views.delete_costumer, name='delete_costumer'),
    path('update-cliente/<int:id>/', views.update_costumer, name='update_costumer'),
]