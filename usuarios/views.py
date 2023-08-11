from django.shortcuts import render,redirect

from django.contrib import messages
from django.contrib.messages import constants

#from django.contrib.auth.models import User

from usuarios.models import CustomUser

from brutils import is_valid_cpf, format_cpf, remove_symbols_cpf

def novo(request):
    if request.user.is_authenticated:

        return render(request, 'novo_usuario.html', {'edit': False})
    else:
        messages.add_message(request, constants.ERROR, 'Você precisa estar autenticado para acessar esta página.')
        return redirect('/')

def gerenciar(request):

    if request.user.is_authenticated:

        nome = request.GET.get('nome')
        
        if nome:
            usuarios = CustomUser.objects.filter(username__icontains=nome).order_by('-id')
        else:
            usuarios = CustomUser.objects.all().order_by('-id')

        return render(request, 'gerenciar_usuarios.html', 
        {'usuarios': usuarios})
    
    else:
        messages.add_message(request, constants.ERROR, 'Você precisa estar autenticado para acessar esta página.')
        return redirect('/')

def cadastrar_usuario(request):

    if request.user.is_authenticated:

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

        emailExist = CustomUser.objects.filter(email__iexact=dados['email'])
        usernameExist = CustomUser.objects.filter(username__iexact=dados['nome'])

        cpfWithOutSimbols = remove_symbols_cpf(dados['cpf'])
        cpfFormated = format_cpf(cpfWithOutSimbols)

        cpfExist = CustomUser.objects.filter(cpf=cpfFormated)

        if not is_valid_cpf(cpfWithOutSimbols):

            messages.add_message(request, constants.ERROR, 'CPF inválido.')
            return redirect('/usuario/novo')
        
        elif len(emailExist) >= 1:

            messages.add_message(request, constants.ERROR, 'O email informado já foi cadastrado.')
            return redirect('/usuario/novo')
        
        elif len(usernameExist) >= 1:

            messages.add_message(request, constants.ERROR, 'O nome de usuario informado ja existe.')
            return redirect('/usuario/novo')
        
        elif len(cpfExist) >= 1:

            messages.add_message(request, constants.ERROR, 'O CPF informado ja foi cadastrado.')
            return redirect('/usuario/novo')
        
        else:

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
            
            user = CustomUser.objects.create_user(
                dados['nome'], 
                dados['email'], 
                dados['password'],
                is_staff = dados['nivel'],
                is_active = dados['status'],
                cpf = cpfFormated,
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

            usuario = CustomUser.objects.get(id=id)

            usuario.is_active = not usuario.is_active

            usuario.save()

            if usuario.is_active:
                messages.add_message(request, constants.SUCCESS, f"O usuario(a) {usuario.username} foi ativado com sucesso!")
            else:
                messages.add_message(request, constants.SUCCESS, f"O usuario(a) {usuario.username} foi inativado com sucesso!")

        except CustomUser.DoesNotExist:

            messages.add_message(request, constants.ERROR, "O usuario(a) informada não existe!")

        return redirect('/usuario/gerenciar')
    else:
        messages.add_message(request, constants.ERROR, 'Você precisa estar autenticado para acessar esta página.')
        return redirect('/')
    
def editar_usuario(request, id):


    if request.user.is_authenticated:

        if (request.method == 'GET'):

            try:

                usuario = CustomUser.objects.get(id=id)

                return render(request, 'novo_usuario.html', {'id': id, 'edit': True, 'usuario': usuario})
            except CustomUser.DoesNotExist:
                messages.add_message(request, constants.ERROR, 'O usuario informado não existe.')
                return redirect('/usuario/gerenciar')
            
        elif (request.method == 'POST'):
            
            dados = {
                'nome': request.POST.get('nome'),
                'email': request.POST.get('email'),
                'telefone': request.POST.get('telefone'),
                'cpf': request.POST.get('cpf'),
                'nivel': request.POST.get('nivel'),
                'status': request.POST.get('status'),
            }

            
            for dado in dados:
                if len(dados[dado].strip()) == 0:
                    messages.add_message(request, constants.ERROR, "Preencha todos os campos!")
                    return redirect(f'/usuario/editar_usuario/{id}')

            try:

                usuario = CustomUser.objects.get(id=id)

                emailExist = CustomUser.objects.filter(email__iexact=dados['email'])
                usernameExist = CustomUser.objects.filter(username__iexact=dados['nome'])

                cpfWithOutSimbols = remove_symbols_cpf(dados['cpf'])

                cpfFormated = format_cpf(cpfWithOutSimbols)

                cpfExist = CustomUser.objects.filter(cpf=cpfFormated)

                if not is_valid_cpf(cpfWithOutSimbols):
                    
                    print('CPF INVALIDO')
                    messages.add_message(request, constants.ERROR, 'CPF inválido.')
                    return redirect(f'/usuario/editar_usuario/{usuario.id}')
                
                elif emailExist and emailExist[0].id != usuario.id:
                    messages.add_message(request, constants.ERROR, 'O email informado já foi cadastrado.')
                    return redirect(f'/usuario/editar_usuario/{usuario.id}')

                elif usernameExist and usernameExist[0].id != usuario.id:
                    messages.add_message(request, constants.ERROR, 'O nome de usuario informado ja existe.')
                    return redirect(f'/usuario/editar_usuario/{usuario.id}')
                
                elif cpfExist and cpfExist[0].id != usuario.id:
                    messages.add_message(request, constants.ERROR, 'O CPF informado ja foi cadastrado.')
                    return redirect(f'/usuario/editar_usuario/{usuario.id}')
                
                else:

                    if dados['status'] == '1':
                        dados['status'] = True
                    else:
                        dados['status'] = False

                    if dados['nivel'] == '2':
                        dados['nivel'] = True
                    else:
                        dados['nivel'] = False
                   
                    usuario.username = dados['nome']
                    usuario.email = dados['email']
                    usuario.telefone = dados['telefone']
                    usuario.cpf = dados['cpf']
                    usuario.is_staff = dados['nivel']
                    usuario.is_active = dados['status']

                    usuario.save()

                    return redirect('/usuario/gerenciar')
                        
            except CustomUser.DoesNotExist:
                messages.add_message(request, constants.ERROR, 'O usuario informado não existe.')
                return redirect('/usuario/gerenciar')
            
    else:
        messages.add_message(request, constants.ERROR, 'Você precisa estar autenticado para acessar esta página.')
        return redirect('/')
    
def detalhes_usuario(request, id):

    if request.user.is_authenticated:
        try:
            user = CustomUser.objects.get(id=id)

            return render(request, 'detalhes_usuario.html', {'usuario': user})
        except CustomUser.DoesNotExist:
            messages.add_message(request, constants.ERROR, 'O usuario informado não existe.')
            return redirect('/usuario/gerenciar')
    else:
        messages.add_message(request, constants.ERROR, 'Você precisa estar autenticado para acessar esta página.')
        return redirect('/')