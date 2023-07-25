from django.shortcuts import render, redirect

from django.contrib.messages import constants
from django.contrib import messages

from .models import Professor

def novo(request):
    return render(request, 'novoProfessor.html')

def gerenciar(request):

    professor = request.GET.get('nome')

    if professor:
        professores = Professor.objects.filter(nome=professor).order_by('-id')
        professoresLen = len(professores)
        return render(request, 'gerenciarProfessores.html', {'professores': professores, 'professoresLen': professoresLen})
    else:
        professores = Professor.objects.all().order_by('-id')
        return render(request, 'gerenciarProfessores.html', {'professores': professores})


def cadastrar_professor(request):

    dados = {
        'nome': request.POST.get('nome'),
        'cpf': request.POST.get('cpf'),
        'registro': request.POST.get('registro'),
        'telefone': request.POST.get('telefone'),
        'email': request.POST.get('email'),
    }

    for dado in dados:
        if len(dados[dado].strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos!')
            return redirect('/professores/novo')
        

    professor = Professor(
        nome = dados['nome'],
        cpf = dados['cpf'],
        registro = dados['registro'],
        telefone = dados['telefone'],
        email = dados['email']
    )

    professor.save()

    messages.add_message(request, constants.SUCCESS, f'Professor {dados["nome"]} cadastrado com sucesso!')
    
    return redirect('/professores/novo')


def alterar_status_professor(request, id):

    try:
        professor = Professor.objects.get(id=id)

        professor.status = not professor.status

        professor.save()

        if professor.status:
            messages.add_message(request, constants.SUCCESS, f'O professor(a) {professor.nome} foi ativado com sucesso!')
        else:
            messages.add_message(request, constants.SUCCESS, f'O professor(a) {professor.nome} foi inativado com sucesso!')

    except Professor.DoesNotExist:

        messages.add_message(request, constants.ERROR, 'O professor informado não existe!')
    return redirect('/professores/gerenciar')