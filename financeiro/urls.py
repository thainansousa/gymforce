from django.urls import path
from . import views

urlpatterns = [
    path('novo', views.novo, name="novaMensalidade"),
    path('gerenciar', views.gerenciar, name="gerenciarMensalidades")
]