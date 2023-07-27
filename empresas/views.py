from django.shortcuts import render, redirect

from django.contrib.messages import constants
from django.contrib import messages

from .models import Empresa

def novo(request):

    return render(request, 'nova_empresa.html')

def gerenciar(request):

    empresas = Empresa.objects.all().order_by('-id')

    return render(request, 'gerenciar_empresas.html', {'empresas': empresas})

def cadastrar_empresa(request):

        dados = {
        'razaoSocial': request.POST.get('razaoSocial'),
        'fantasia': request.POST.get('fantasia'),
        'cnpj': request.POST.get('cnpj')
    }

        for dado in dados:
            if len(dados[dado].strip()) == 0:
                messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
                return redirect('/empresas/novo')

        empresa = Empresa(
            razaoSocial = dados['razaoSocial'],
            fantasia = dados['fantasia'],
            cnpj = dados['cnpj']
        )

        empresa.save()

        messages.add_message(request, constants.SUCCESS, 'Empresa cadastrada com sucesso!')

        return redirect('/empresas/novo')

def alterar_status_empresa(request, id):


    try:

        empresa = Empresa.objects.get(id=id)

        empresa.status = not empresa.status

        empresa.save()


        if empresa.status:
            messages.add_message(request, constants.SUCCESS, f'A empresa {empresa.razaoSocial} foi ativada com sucesso!')
        else:
            messages.add_message(request, constants.SUCCESS, f'A empresa {empresa.razaoSocial} foi inativada com sucesso!')

    except Empresa.DoesNotExist:
        messages.add_message(request, constants.ERROR, "A empresa informada não existe!")
    
    return redirect('/empresas/gerenciar')