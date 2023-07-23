from django.shortcuts import render, redirect

from .models import Mensalidade

from django.contrib.messages import constants
from django.contrib import messages

def novo(request):
    return render(request, 'nova_mensalidade.html')

def gerenciar(request):

    nome = request.GET.get('plano')

    if nome:
        mensalidades = Mensalidade.objects.filter(nome=nome)
        return render(request, 'gerenciar_mensalidades.html', {'mensalidades': mensalidades})
    else:
        mensalidades = Mensalidade.objects.all().order_by('-id')
        return render(request, 'gerenciar_mensalidades.html', {'mensalidades': mensalidades})


def cadastrar_mensalidade(request):
    
    dados = {
        'nome_do_plano': request.POST.get('plano'),
        'valor': request.POST.get('valor')
    }

    for dado in dados:
        if len(dados[dado].strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos!')
            return redirect('/financeiro/novo')

    mensalidade = Mensalidade(
        nome = dados['nome_do_plano'],
        valor = dados['valor']
    )

    mensalidade.save()
        
    messages.add_message(request, constants.SUCCESS, 'Mensalidade cadastrada com sucesso!')

    return redirect('/financeiro/novo')



def alterar_status_mensalidade(request, id):

    mensalidade = Mensalidade.objects.get(id=id)

    mensalidade.status = not mensalidade.status

    mensalidade.save()


    if mensalidade.status:
        messages.add_message(request, constants.SUCCESS, 'Mensalidade ativada com sucesso!')
    else:
        messages.add_message(request, constants.SUCCESS, 'Mensalidade inativada com sucesso!')

    return redirect('/financeiro/gerenciar')