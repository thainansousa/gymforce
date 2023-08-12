from django.shortcuts import render, redirect

from django.contrib.messages import constants
from django.contrib import messages

from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user

from usuarios.models import CustomUser

from .models import RecuperarSenha

def login(request):
    return render(request, 'login.html')


def auth(request):

    username = request.POST.get('username')
    password = request.POST.get('password')

    if len(username.strip()) == 0 or len(password.strip()) == 0:
        messages.add_message(request, constants.ERROR, 'Preencha todos os campos!')
        return redirect('/')
    else:
        user = authenticate(username=username, password=password)

        if user is not None:
            login_user(request, user)
            return redirect('/home')
        else:
            messages.add_message(request, constants.ERROR, 'Email ou senha invalidos!')
            return redirect('/')

def logout(request):
    logout_user(request)

    return redirect('/')

def recuperar_senha(request):
    if (request.method) == 'GET':
        return render(request, 'recuperar_senha.html')
    elif (request.method) == 'POST':

        email = request.POST.get('email')

        try:

            user = CustomUser.objects.get(email__iexact=email)

            reset = RecuperarSenha(
                user_id = user.id
            )

            reset.save()

            messages.add_message(request, constants.ERROR, 'Token para recuperação de senha gerado com sucesso.')

            return redirect('/')

        except CustomUser.DoesNotExist:
            messages.add_message(request, constants.ERROR, 'O email informado não existe.')
            return redirect('/')
