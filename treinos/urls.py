from django.urls import path
from . import views

urlpatterns = [
    path('novo/', views.novo, name="novoTreino"),
    path('gerenciar/', views.gerenciar, name="gerenciarTreinos"),
    path('cadastrar_treino/', views.cadastrar_treino, name="cadastrarTreino"),
    path('alterar_status_treino/<int:id>', views.alterar_status_treino, name="alterarStatusTreino"),
    path('editar_treino/<int:id>', views.editar_treino, name="editarTreino")
]