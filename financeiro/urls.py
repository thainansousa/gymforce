from django.urls import path
from . import views

urlpatterns = [
    path('novo/', views.novo, name="novaMensalidade"),
    path('gerenciar/', views.gerenciar, name="gerenciarMensalidades"),
    path('cadastrar_mensalidade/', views.cadastrar_mensalidade, name="cadastrarMensalidade"),
    path('alterar_status_mensalidade/<int:id>', views.alterar_status_mensalidade, name='alterar_status_mensalidade'),
    path('editar_plano_mensalidade/<int:id>', views.editar_plano_mensalidade, name='editarPlanoMensalidade')
]