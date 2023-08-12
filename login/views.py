from django.shortcuts import render, redirect

from django.contrib.messages import constants
from django.contrib import messages

from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user

from usuarios.models import CustomUser

from .models import RecuperarSenha

from django.core.mail import send_mail

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
                user_id = user.id,
            )

            reset.save()

            tokenFormated = str(reset.token)
            
            print(tokenFormated)

            messages.add_message(request, constants.SUCCESS, 'Informe o token printado no console e sua nova senha.')
            return redirect('/recuperar_senha/token')

        except CustomUser.DoesNotExist:
            messages.add_message(request, constants.ERROR, 'O email informado não existe.')
            return redirect('/')
        
def token_auth(request):
    if (request.method) == 'GET':
        return render(request, 'alterar_senha.html')
    elif (request.method) == 'POST':
        
        user_token = request.POST.get('token')
        newPassword = request.POST.get('password')

        if len(user_token.strip()) == 0 or len(newPassword.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos.')
            return redirect('/recuperar_senha/token/')
        
        try:

            tk = RecuperarSenha.objects.get(token=str(user_token))

            if tk:
                if not tk.status:

                    user = CustomUser.objects.get(id=tk.user_id)

                    user.set_password(newPassword)

                    user.save()

                    messages.add_message(request, constants.SUCCESS, 'Senha alterada com sucesso.')

                    tk.status = not tk.status

                    tk.save()

                    return redirect('/')
                else:
                    messages.add_message(request, constants.ERROR, 'O token informado expirou.')
                    return redirect('/')
        except RecuperarSenha.DoesNotExist:
            messages.add_message(request, constants.ERROR, 'O token não existe.')
            return redirect('/')

        