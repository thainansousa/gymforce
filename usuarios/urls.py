from django.urls import path
from . import views

urlpatterns = [
    path('novo/', views.novo, name='novoUsuario'),
    path('gerenciar/', views.gerenciar, name='gerenciarUsuario'),
    path('cadastrar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('deletar_usuario/<int:id>', views.deletar_usuario, name='deletar_usuario')
]