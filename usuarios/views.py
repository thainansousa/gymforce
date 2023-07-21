from django.shortcuts import render

def novoUsuario(request):
    return render(request, 'novo.html')

def gerenciarUsuario(request):
    return render(request, 'gerenciar.html')
