from django.urls import path
from . import views

urlpatterns = [
    path('novo/', views.novo, name='novaEmpresa'),
    path('gerenciar/', views.gerenciar, name='gerenciarEmpresas'),
    path('cadastrar_empresa/', views.cadastrar_empresa, name='cadastrarEmpresa'),
    path('alterar_status_empresa/<int:id>', views.alterar_status_empresa, name='alterarStatusEmpresa'),
    path('editar_empresa/<int:id>', views.editar_empresa, name="editarEmpresa"),
    path('detalhes_empresa/<int:id>', views.detalhes_empresa, name='detalhesEmpresa')
]