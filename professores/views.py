from django.shortcuts import render

def novo(request):
    return render(request, 'novoProfessor.html')

def gerenciar(request):
    return render(request, 'gerenciarProfessores.html')
