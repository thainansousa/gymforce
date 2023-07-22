from django.shortcuts import render

def novo(request):
    return render(request, 'novo_usuario.html')

def gerenciar(request):
    return render(request, 'gerenciar_usuarios.html')
