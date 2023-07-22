from django.urls import path
from . import views

urlpatterns = [
    path('novo', views.novo, name="novoProfessor"),
    path('gerenciar', views.gerenciar, name="gerenciarProfessores")
]