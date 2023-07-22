from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('usuario/', include('usuarios.urls')),
    path('alunos/', include('alunos.urls')),
    path('professores/', include('professores.urls')),
    path('treinos/', include('treinos.urls')),
    path('financeiro/', include('financeiro.urls'))
]
