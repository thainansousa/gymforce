from django.urls import path
from . import views

urlpatterns = [
    path('novo/', views.novo, name="novoProfessor"),
    path('gerenciar/', views.gerenciar, name="gerenciarProfessores"),
    path('cadastrar_professor',views.cadastrar_professor, name="cadastrarProfessor"),
    path('alterar_status_professor/<int:id>', views.alterar_status_professor, name="alterarStatusProfessor"),
    path('editar_professor/<int:id>', views.editar_professor, name="editarProfessor"),
    path('detalhes_professor/<int:id>', views.detalhes_professor, name="detalhesProfessor"),
    path('gerar_relatorio_professores', views.gerar_relatorio_professores, name="gerarRelatorioProfessores")
]