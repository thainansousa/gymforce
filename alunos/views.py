from django.shortcuts import render, redirect

from financeiro.models import Mensalidade
from .models import Aluno
from django.contrib.messages import constants
from django.contrib import messages

def novo(request):

    mensalidades = Mensalidade.objects.all()

    return render(request, 'novo_aluno.html', {'mensalidades': mensalidades})

def gerenciar(request):

    aluno = request.GET.get('nome')

    if aluno:
        alunos = Aluno.objects.filter(nome=aluno)
        alunosLen = len(alunos)
    else:
        alunos = Aluno.objects.all().order_by('-id')
        alunosLen = len(alunos)

    return render(request, 'gerenciar_alunos.html', {'alunos': alunos, 'alunosLen': alunosLen})


def cadastrar_aluno(request):

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


def alterar_status_aluno(request, id):

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