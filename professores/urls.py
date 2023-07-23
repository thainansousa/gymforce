from django.urls import path
from . import views

urlpatterns = [
    path('novo/', views.novo, name="novoProfessor"),
    path('gerenciar/', views.gerenciar, name="gerenciarProfessores"),
    path('cadastrar_professor',views.cadastrar_professor, name="cadastrarProfessor"),
    path('alterar_status_professor/<int:id>', views.alterar_status_professor, name="alterarStatusProfessor")
]