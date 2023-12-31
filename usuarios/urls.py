from django.urls import path
from . import views

urlpatterns = [
    path('novo/', views.novo, name='novoUsuario'),
    path('gerenciar/', views.gerenciar, name='gerenciarUsuario'),
    path('cadastrar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('alterar_status_usuario/<int:id>', views.alterar_status_usuario, name='alterar_status_usuario'),
    path('editar_usuario/<int:id>', views.editar_usuario, name='editarUsuario'),
    path('detalhes_usuario/<int:id>', views.detalhes_usuario, name="detalhesUsuario")
]