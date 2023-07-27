from django.shortcuts import render

def novo(request):

    return render(request, 'nova_empresa.html')

def gerenciar(request):

    return