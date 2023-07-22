from django.shortcuts import render

def novo(request):
    return render(request, 'nova_mensalidade.html')

def gerenciar(request):
    return render(request, 'gerenciar_mensalidades.html')
