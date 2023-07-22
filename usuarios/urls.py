from django.urls import path
from . import views

urlpatterns = [
    path('novo', views.novo, name='novoUsuario'),
    path('gerenciar', views.gerenciar, name='gerenciarUsuario')
]