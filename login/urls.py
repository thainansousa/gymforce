from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('auth/', views.auth, name="auth"),
    path('logout/', views.logout, name="logout"),
    path('recuperar_senha/', views.recuperar_senha, name="recuperarSenha"),
    path('recuperar_senha/token/', views.token_auth, name="tokenAuth")
]