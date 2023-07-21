from django.urls import path
from . import views

urlpatterns = [
    path('novo', views.novoUsuario, name='novoUsuario'),
    path('gerenciar', views.gerenciarUsuario, name='gerenciarUsuario')
]