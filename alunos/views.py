import os

from django.shortcuts import render, redirect

from financeiro.models import Mensalidade
from .models import Aluno
from treinos.models import Treino, Treino_Aluno
from django.contrib.messages import constants
from django.contrib import messages

from datetime import datetime

from django.conf import settings

from io import BytesIO

from django.template.loader import render_to_string

from weasyprint import HTML

from django.http import FileResponse

from templates.services.calcularDiaDaSemana import calcularDiaDaSemana

from brutils import remove_symbols_cpf, is_valid_cpf, format_cpf

import re

def novo(request):

    if request.user.is_authenticated:
        mensalidades = Mensalidade.objects.filter(status=True)

        return render(request, 'novo_aluno.html', {'mensalidades': mensalidades, 'edit': False})
    else:
        messages.add_message(request, constants.ERROR, 'Você precisa estar autenticado para acessar esta página.')
        return redirect('/')

def gerenciar(request):

    if request.user.is_authenticated:
        aluno = request.GET.get('name')

        if aluno:
            alunos = Aluno.objects.filter(nome__iexact=aluno).order_by('-id')
        else:
            alunos = Aluno.objects.all().order_by('-id')

        return render(request, 'gerenciar_alunos.html', {'alunos': alunos})
    else:
        messages.add_message(request, constants.ERROR, 'Você precisa estar autenticado para acessar esta página.')
        return redirect('/')



def cadastrar_aluno(request):

    if request.user.is_authenticated:

        dados = {
        'nome': request.POST.get('nome'),
        'rg': request.POST.get('rg'),
        'dt_nasc': request.POST.get('dt_nasc'),
        'cpf': request.POST.get('cpf'),
        'telefone': request.POST.get('telefone'),
        'email': request.POST.get('email'),
        'mensalidade': request.POST.get('mensalidade')
    }


        for dado in dados:
            if len(dados[dado].strip()) == 0:
                messages.add_message(request, constants.ERROR, 'Preencha todos os campos!')
                return redirect('/alunos/novo')
            

        cpfWithOutSymbols = remove_symbols_cpf(dados['cpf'])

        cpfIsValid = is_valid_cpf(cpfWithOutSymbols)

        cpfFormated = format_cpf(cpfWithOutSymbols)

        emailExist = Aluno.objects.filter(email__iexact=dados['email'])
        cpfExist = Aluno.objects.filter(cpf__iexact=cpfFormated)

        rgPattern = re.compile("[0-9]+")

        rgIsValid = re.fullmatch(rgPattern, dados['rg'])


        if not cpfIsValid:
            messages.add_message(request, constants.ERROR, 'O CPF informado não é valido.')
            return redirect('/alunos/novo/')
        elif emailExist:
            messages.add_message(request, constants.ERROR, 'O email informado já foi cadastrado.')
            return redirect('/alunos/novo/')
        elif cpfExist:
            messages.add_message(request, constants.ERROR, 'O CPF informado já foi cadastrado.')
            return redirect('/alunos/novo/')
        elif rgIsValid == None:
            messages.add_message(request, constants.ERROR, 'Informe apenas os números do RG.')
            return redirect('/alunos/novo/')
        else:

            alunos = Aluno(
                nome = dados['nome'],
                rg = dados['rg'],
                cpf = dados['cpf'],
                data_nascimento = dados['dt_nasc'],
                telefone = dados['telefone'],
                email = dados['email'],
                mensalidade_id = dados['mensalidade']
            )

            alunos.save()

            messages.add_message(request, constants.SUCCESS, f'Aluno(a) {dados["nome"]} cadastrado com sucesso!')

            return redirect('/alunos/novo')
    else:
        messages.add_message(request, constants.ERROR, 'Você precisa estar autenticado para acessar esta página.')
        return redirect('/')


def alterar_status_aluno(request, id):

    if request.user.is_authenticated:
        try:
            aluno = Aluno.objects.get(id=id)

            aluno.status = not aluno.status

            aluno.save()

            if aluno.status:
                messages.add_message(request, constants.SUCCESS, f'O aluno(a) {aluno.nome} foi ativado com sucesso!')
            else:
                messages.add_message(request, constants.SUCCESS, f'O aluno(a) {aluno.nome} foi inativado com sucesso!')
    
        except Aluno.DoesNotExist:
            messages.add_message(request, constants.ERROR, f'O aluno informado não existe!')

    
        return redirect('/alunos/gerenciar')
    else:
        messages.add_message(request, constants.ERROR, 'Você precisa estar autenticado para acessar esta página.')
        return redirect('/')


def gerenciarTreinoAluno(request, id):

    if request.user.is_authenticated:

        if (request.method == 'GET'):

            try:
                aluno = Aluno.objects.get(id=id)
                treinos = Treino.objects.all()
                treinos_aluno = Treino_Aluno.objects.filter(aluno_id=id).order_by('-id')
            except Aluno.DoesNotExist:

                messages.add_message(request, constants.ERROR, 'O aluno informado não existe!')

                return redirect(f'/alunos/gerenciar/')

            return render(request, 'gerenciar_treino_alunos.html', {
                'aluno': aluno, 
                'treinos': treinos, 
                'treinos_aluno': treinos_aluno})
        
        elif (request.method == 'POST'):


            print(request.POST.get('series'))

            dados = {
                'treino_id': request.POST.get('treino'),
                'series': request.POST.get('series'),
                'rept': request.POST.get('rept'),
                'dia_semana': request.POST.get('dia_semana')
            }

            for dado in dados:
                if len(dados[dado].strip()) == 0:
                    messages.add_message(request, constants.ERROR, 'Preencha todos os campos!')
                    return redirect(f'/alunos/gerenciar/treinos/{id}')


            treino_aluno = Treino_Aluno(
                treino_id = dados['treino_id'],
                treino_series = dados['series'],
                treino_qtd = dados['rept'],
                treino_dia = dados['dia_semana'],
                aluno_id = id
            )

            treino_aluno.save()

            messages.add_message(request, constants.SUCCESS, 'Treino do aluno cadastrado com sucesso!')

            return redirect(f'/alunos/gerenciar/treinos/{id}')
    else:
        messages.add_message(request, constants.ERROR, 'Você precisa estar autenticado para acessar esta página.')
        return redirect('/')

def excluir_treino_aluno(request, id):

    if request.user.is_authenticated:
        try:
            treino_aluno = Treino_Aluno.objects.get(id=id)

            treino_aluno.delete()

            messages.add_message(request, constants.ERROR, 'Treino removido para este aluno!')

            return redirect(f'/alunos/gerenciar/treinos/{treino_aluno.aluno_id}')

        except Treino_Aluno.DoesNotExist:

            messages.add_message(request, constants.ERROR, 'O aluno não possui esse treino cadastrado!')
    
            return redirect(f'/alunos/gerenciar/')
    else:
        messages.add_message(request, constants.ERROR, 'Você precisa estar autenticado para acessar esta página.')
        return redirect('/')
    

def imprimir_treino_aluno(request, id):
    
    if request.user.is_authenticated:

        diaDaSemana = datetime.now().weekday()

        diaFormatado = calcularDiaDaSemana(diaDaSemana)

        treino_dia = Treino_Aluno.objects.filter(aluno_id=id, treino_dia=diaFormatado)

        if len(treino_dia) > 0:

            aluno  = Aluno.objects.get(id=id)

            path_template = os.path.join(settings.BASE_DIR, 'templates/partials/treino_aluno.html')
            path_output = BytesIO()

            template_render = render_to_string(path_template, {'treinos': treino_dia, 'aluno': aluno.nome})

            HTML(string=template_render).write_pdf(path_output)

            path_output.seek(0)

            return FileResponse(path_output, filename=f"Treino do dia para {aluno.nome}.pdf")
        else:
            messages.add_message(request, constants.ERROR, 'O aluno não tem treinos cadastrados para hoje!')
            return redirect(f'/alunos/gerenciar/treinos/{id}')

    else:
        messages.add_message(request, constants.ERROR, 'Você precisa estar autenticado para acessar esta página.')
        return redirect('/')
    
def editar_aluno(request, id):

    if request.user.is_authenticated:
        if (request.method) == 'GET':
            try:
                aluno = Aluno.objects.get(id=id)
                mensalidades = Mensalidade.objects.filter(status=True)
                return render(request, 'novo_aluno.html', {'edit': True, 'aluno': aluno, 'mensalidades': mensalidades})
            except Aluno.DoesNotExist:
                messages.add_message(request, constants.ERROR, 'O aluno informado não existe.')
                return redirect('/alunos/gerenciar')
        else:
            try:
                aluno = Aluno.objects.get(id=id)

                dados = {
                    'nome': request.POST.get('nome'),
                    'rg': request.POST.get('rg'),
                    'cpf': request.POST.get('cpf'),
                    'telefone': request.POST.get('telefone'),
                    'email': request.POST.get('email'),
                    'mensalidade': request.POST.get('mensalidade')
                }

                for dado in dados:
                    if len(dados[dado].strip()) == 0:
                        messages.add_message(request, constants.ERROR, 'Preencha todos os campos!')
                        return redirect(f'/alunos/editar_aluno/{aluno.id}')
                
                cpfWithOutSymbols = remove_symbols_cpf(dados['cpf'])

                cpfIsValid = is_valid_cpf(cpfWithOutSymbols)

                cpfFormated = format_cpf(cpfWithOutSymbols)

                emailExist = Aluno.objects.filter(email__iexact=dados['email'])
                cpfExist = Aluno.objects.filter(cpf=cpfFormated)

                rgPattern = re.compile("[0-9]+")

                rgIsValid = re.fullmatch(rgPattern, dados['rg'])

                if not cpfIsValid:
                    messages.add_message(request, constants.ERROR, 'O CPF informado não é valido.')
                    return redirect(f'/alunos/editar_aluno/{aluno.id}')
                elif emailExist and emailExist[0].id != aluno.id:
                    messages.add_message(request, constants.ERROR, 'O email informado já foi cadastrado.')
                    return redirect(f'/alunos/editar_aluno/{aluno.id}')
                elif cpfExist and cpfExist[0].id != aluno.id:
                    messages.add_message(request, constants.ERROR, 'O CPF informado já foi cadastrado.')
                    return redirect(f'/alunos/editar_aluno/{aluno.id}')
                elif rgIsValid == None:
                    messages.add_message(request, constants.ERROR, 'Informe apenas os números do RG.')
                    return redirect(f'/alunos/editar_aluno/{aluno.id}')
                else:
                    aluno.nome = dados['nome']
                    aluno.rg = dados['rg']
                    aluno.cpf = cpfFormated
                    aluno.telefone = dados['telefone']
                    aluno.email = dados['email']
                    aluno.mensalidade_id = dados['mensalidade']

                    aluno.save()

                    messages.add_message(request, constants.SUCCESS, f'O aluno {aluno.nome} foi editado com sucesso.')
                    return redirect('/alunos/gerenciar/')
                
            except Aluno.DoesNotExist:
                messages.add_message(request, constants.ERROR, 'O aluno informado não existe.')
                return redirect('/alunos/gerenciar')
    else:
        messages.add_message(request, constants.ERROR, 'Você precisa estar autenticado para acessar esta página.')
        return redirect('/')
    
def detalhes_aluno(request, id):

    if request.user.is_authenticated:
        try:
            aluno = Aluno.objects.get(id=id)

            return render(request, 'detalhes_aluno.html', {'aluno': aluno})
        
        except Aluno.DoesNotExist:

            messages.add_message(request, constants.ERROR, 'O aluno informado não existe.')
            return redirect('/alunos/gerenciar')
    else:
        
        messages.add_message(request, constants.ERROR, 'Você precisa estar autenticado para acessar esta página.')
        return redirect('/')