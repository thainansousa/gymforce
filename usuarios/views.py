from django.shortcuts import render,redirect

from django.contrib import messages
from django.contrib.messages import constants

from .models import Usuario

def novo(request):
    return render(request, 'novo_usuario.html')

def gerenciar(request):

    nome = request.GET.get('nome')

    if nome:
        usuarios = Usuario.objects.filter(nome=nome).order_by('-id')
        usuariosLen = len(usuarios)
    else:
        usuarios = Usuario.objects.all().order_by('-id')
        usuariosLen = len(usuarios)

    return render(request, 'gerenciar_usuarios.html', 
    {'usuarios': usuarios,
     'usuariosLen': usuariosLen})

def cadastrar_usuario(request):

    dados = {
        'nome': request.POST.get('nome'),
        'email': request.POST.get('email'),
        'telefone': request.POST.get('telefone'),
        'cpf': request.POST.get('cpf'),
        'password': request.POST.get('password'),
        'password2': request.POST.get('password2'),
        'nivel': request.POST.get('nivel'),
        'status': request.POST.get('status'),
    }

    for i in dados:
        if len(dados[i].strip()) == 0:
            messages.add_message(request, constants.ERROR, "Preencha todos os campos!")
            return redirect('/usuario/novo')
        
    if dados['password'] != dados['password2']:
        messages.add_message(request, constants.ERROR, "As senhas não combinam, tente novamente.")
        return redirect('/usuario/novo')

    if dados['status'] == '1':
        dados['status'] = True
    else:
        dados['status'] = False

    usuario = Usuario(
        nome = dados['nome'],
        email = dados['email'],
        password = dados['password'],
        telefone = dados['telefone'],
        cpf = dados['cpf'],
        nivel_administrativo = dados['nivel'],
        status = dados['status']
    )
    
    usuario.save()
    messages.add_message(request, constants.SUCCESS, "Cadastrado com sucesso!")

    return redirect('/usuario/novo')


def deletar_usuario(request, id):
    usuario = Usuario.objects.get(id=id)

    usuario.delete()

    messages.add_message(request, constants.SUCCESS, "Usuario deletado com sucesso!")

    return redirect('/usuario/gerenciar')