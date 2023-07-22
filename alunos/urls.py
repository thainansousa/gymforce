from django.urls import path
from . import views

urlpatterns = [
    path('novo', views.novo, name="novoAluno"),
    path('gerenciar', views.gerenciar, name="gerenciarAluno")
]