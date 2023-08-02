from django.shortcuts import render,redirect

from django.contrib import messages
from django.contrib.messages import constants

#from .models import Usuario

from django.contrib.auth.models import User

def novo(request):
    if request.user.is_authenticated:

        return render(request, 'novo_usuario.html')
    else:
        messages.add_message(request, constants.ERROR, 'Você precisa estar autenticado para acessar esta página.')
        return redirect('/')

def gerenciar(request):

    if request.user.is_authenticated:

        nome = request.GET.get('nome')
        
        if nome:
            nome.lower()
            usuarios = User.objects.filter(email=nome).order_by('-id')
        else:
            usuarios = User.objects.all().order_by('-id')

        return render(request, 'gerenciar_usuarios.html', 
        {'usuarios': usuarios})
    
    else:
        messages.add_message(request, constants.ERROR, 'Você precisa estar autenticado para acessar esta página.')
        return redirect('/')

def cadastrar_usuario(request):

    if request.user.is_authenticated:

        dados = {
            'nome': request.POST.get('nome').lower(),
            'email': request.POST.get('email').lower(),
            'telefone': request.POST.get('telefone'),
            'cpf': request.POST.get('cpf'),
            'password': request.POST.get('password'),
            'password2': request.POST.get('password2'),
            'nivel': request.POST.get('nivel'),
            'status': request.POST.get('status'),
        }

        emailExist = User.objects.filter(email=dados['email'])
        usernameExist = User.objects.filter(username=dados['nome'])

        if len(emailExist) >= 1:
            messages.add_message(request, constants.ERROR, 'O email informado já foi cadastrado.')
            return redirect('/usuario/novo')
        
        if len(usernameExist) >= 1:
            messages.add_message(request, constants.ERROR, 'O nome de usuario informado ja existe.')
            return redirect('/usuario/novo')

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


        if dados['nivel'] == '2':
            dados['nivel'] = True
        else:
            dados['nivel'] = False
        
        user = User.objects.create_user(
            dados['nome'], 
            dados['email'], 
            dados['password'],
            is_staff = dados['nivel'],
            is_active = dados['status'],
            cpf = dados['cpf'],
            telefone = dados['telefone'])

        user.save()

        messages.add_message(request, constants.SUCCESS, f"Usuario {dados['nome']} cadastrado com sucesso!")

        return redirect('/usuario/novo')
    else:
        messages.add_message(request, constants.ERROR, 'Você precisa estar autenticado para acessar esta página.')
        return redirect('/')

def alterar_status_usuario(request, id):

    if request.user.is_authenticated:

        try:

            usuario = User.objects.get(id=id)

            usuario.is_active = not usuario.is_active

            usuario.save()

            if usuario.is_active:
                messages.add_message(request, constants.SUCCESS, f"O usuario(a) {usuario.username} foi ativado com sucesso!")
            else:
                messages.add_message(request, constants.SUCCESS, f"O usuario(a) {usuario.username} foi inativado com sucesso!")

        except User.DoesNotExist:

            messages.add_message(request, constants.ERROR, "O usuario(a) informada não existe!")

        return redirect('/usuario/gerenciar')
    else:
        messages.add_message(request, constants.ERROR, 'Você precisa estar autenticado para acessar esta página.')
        return redirect('/')