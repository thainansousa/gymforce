from django.shortcuts import render

def novo(request):
    return render(request, 'novo_aluno.html')

def gerenciar(request):
    return render(request, 'gerenciar_alunos.html')