from django.shortcuts import render,redirect

from django.contrib.messages import constants
from django.contrib import messages

from .models import Treino

def novo(request):
    if request.user.is_authenticated:

        return render(request, 'novo_treino.html', {'edit': False})
    else:
        messages.add_message(request, constants.ERROR, 'Você precisa estar autenticado para acessar esta página.')
        return redirect('/')

def gerenciar(request):

    if request.user.is_authenticated:


        treino = request.GET.get('nome')

        if treino:
            treinos = Treino.objects.filter(nome__iexact=treino).order_by('-id')
        else:
            treinos = Treino.objects.all().order_by('-id')

        return render(request, 'gerenciar_treinos.html', {'treinos': treinos})
    else:
        messages.add_message(request, constants.ERROR, 'Você precisa estar autenticado para acessar esta página.')
        return redirect('/')

def cadastrar_treino(request):

    if request.user.is_authenticated:
        

        nome = request.POST.get('nome')

        if len(nome.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha o campo nome do treino')
            return redirect('/treinos/novo')
        
        treinoExist = Treino.objects.filter(nome__iexact=nome)

        if treinoExist:
            messages.add_message(request, constants.ERROR, 'Esse treino ja foi cadastrado.')
            return redirect('/treinos/novo')
        
        treino = Treino(
            nome = nome
        )

        treino.save()

        messages.add_message(request, constants.SUCCESS, f'Treino {nome} cadastrado com sucesso!')

        return redirect('/treinos/novo')
    else:
        messages.add_message(request, constants.ERROR, 'Você precisa estar autenticado para acessar esta página.')
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
        messages.add_message(request, constants.ERROR, 'Você precisa estar autenticado para acessar esta página.')
        return redirect('/')
    
def editar_treino(request, id):

    if request.user.is_authenticated:
        if (request.method) == 'GET':
            try:
                treino = Treino.objects.get(id=id)
                return render(request, 'novo_treino.html', {'edit': True, 'treino': treino})
            except Treino.DoesNotExist:
                messages.add_message(request, constants.ERROR, 'O treino informado não existe.')
                return redirect('/treinos/gerenciar/')
        else:
            try:
                treino = Treino.objects.get(id=id)

                nome = request.POST.get('nome')

                if len(nome.strip()) == 0:
                    messages.add_message(request, constants.ERROR, 'Preencha todos os campos.')
                    return redirect(f'/treinos/editar_treino/{treino.id}')
                
                treinoExist = Treino.objects.filter(nome__iexact=nome)

                if treinoExist and treinoExist[0].id != treino.id:
                    messages.add_message(request, constants.ERROR, 'Já existe um treino com esse nome.')
                    return redirect(f'/treinos/editar_treino/{treino.id}')
                else:
                    treino.nome = nome

                    treino.save()

                    messages.add_message(request, constants.SUCCESS, 'Treino editado com sucesso.')

                    return redirect('/treinos/gerenciar/')
                
            except Treino.DoesNotExist:
                messages.add_message(request, constants.ERROR, 'O treino informada não existe.')
                return redirect('/treinos/gerenciar')

    else:
        messages.add_message(request, constants.ERROR, 'Você precisa estar autenticado para acessar esta página.')
        return redirect('/')