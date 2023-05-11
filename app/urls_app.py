from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("login/", views.login),
    path("blog/", views.cadastro),
    path("exemplo/", views.exemplo),
]
