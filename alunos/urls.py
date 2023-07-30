from django.urls import path
from . import views

urlpatterns = [
    path('novo/', views.novo, name="novoAluno"),
    path('gerenciar/', views.gerenciar, name="gerenciarAluno"),
    path('cadastrar_aluno/', views.cadastrar_aluno, name="cadastrarAluno"),
    path('alterar_status_aluno/<int:id>', views.alterar_status_aluno, name="alterarStatusAluno"),
    path('gerenciar/treinos/<int:id>', views.gerenciarTreinoAluno, name="gerenciarTreinoAluno"),
    path('excluir_treino_aluno/<int:id>', views.excluir_treino_aluno, name="excluirTreinoAluno"),
    path('imprimir_treino_aluno/<int:id>', views.imprimir_treino_aluno, name="imprimirTreinoAluno")
]