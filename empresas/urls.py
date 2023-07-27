from django.urls import path
from . import views

urlpatterns = [
    path('novo/', views.novo, name='novaEmpresa'),
    path('gerenciar/', views.gerenciar, name='gerenciarEmpresas')
]