from django.shortcuts import render,redirect

from django.contrib.messages import constants
from django.contrib import messages

from .models import Treino

def novo(request):
    if request.user.is_authenticated:

        return render(request, 'novo_treino.html')
    else:
        messages.add_message(request, constants.ERROR, 'Vocẽ precisa estar autenticado para acessar esta página.')
        return redirect('/')

def gerenciar(request):

    if request.user.is_authenticated:


        treino = request.GET.get('nome')

        if treino:
            treinos = Treino.objects.filter(nome=treino).order_by('-id')
            treinosLen = len(treinos)
        else:
            treinos = Treino.objects.all().order_by('-id')
            treinosLen = len(treinos)

        return render(request, 'gerenciar_treinos.html', {'treinos': treinos, 'treinosLen': treinosLen})
    else:
        messages.add_message(request, constants.ERROR, 'Vocẽ precisa estar autenticado para acessar esta página.')
        return redirect('/')

def cadastrar_treino(request):

    if request.user.is_authenticated:
        

        nome = request.POST.get('nome')

        if len(nome.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha o campo nome do treino')
            return redirect('/treinos/novo')
        
        treino = Treino(
            nome = nome
        )

        treino.save()

        messages.add_message(request, constants.SUCCESS, f'Treino {nome} cadastrado com sucesso!')

        return redirect('/treinos/novo')
    else:
        messages.add_message(request, constants.ERROR, 'Vocẽ precisa estar autenticado para acessar esta página.')
        return redirect('/')

def alterar_status_treino(request, id):

    if request.user.is_authenticated:


        try:

            treino = Treino.objects.get(id=id)

            treino.status = not treino.status

            treino.save()

            if treino.status:
                messages.add_message(request, constants.SUCCESS, f'O treino {treino.nome} foi ativado com sucesso!')
            else:
                messages.add_message(request, constants.SUCCESS, f'O treino {treino.nome} foi inativado com sucesso!')
            
        except Treino.DoesNotExist:
            messages.add_message(request, constants.ERROR, 'O treino informado não foi encontrado.')
        
        return redirect('/treinos/gerenciar')
    else:
        messages.add_message(request, constants.ERROR, 'Vocẽ precisa estar autenticado para acessar esta página.')
        return redirect('/')