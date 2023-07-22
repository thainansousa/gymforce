from django.shortcuts import render

def novo(request):
    return render(request, 'novo_treino.html')

def gerenciar(request):
    return render(request, 'gerenciar_treinos.html')
