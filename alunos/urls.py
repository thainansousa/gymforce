from django.urls import path
from . import views

urlpatterns = [
    path('novo/', views.novo, name="novoAluno"),
    path('gerenciar/', views.gerenciar, name="gerenciarAluno"),
    path('cadastrar_aluno/', views.cadastrar_aluno, name="cadastrarAluno"),
    path('alterar_status_aluno/<int:id>', views.alterar_status_aluno, name="alterarStatusAluno")
]