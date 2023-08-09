from django.shortcuts import render, redirect

from django.contrib.messages import constants
from django.contrib import messages

from .models import Professor

from brutils import remove_symbols_cpf, is_valid_cpf, format_cpf

def novo(request):
    if request.user.is_authenticated:
    
        return render(request, 'novoProfessor.html', {'edit': False})
    else:
        messages.add_message(request, constants.ERROR, 'Você precisa estar autenticado para acessar esta página.')
        return redirect('/')

def gerenciar(request):

    if request.user.is_authenticated:

        professor = request.GET.get('nome')

        if professor:
            professores = Professor.objects.filter(nome__iexact=professor).order_by('-id')
            return render(request, 'gerenciarProfessores.html', {'professores': professores})
        else:
            professores = Professor.objects.all().order_by('-id')
            return render(request, 'gerenciarProfessores.html', {'professores': professores})
    else:
        messages.add_message(request, constants.ERROR, 'Você precisa estar autenticado para acessar esta página.')
        return redirect('/')

def cadastrar_professor(request):

    if request.user.is_authenticated:

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
            
        emailExist = Professor.objects.filter(email__iexact=dados['email'])
        registroExist = Professor.objects.filter(registro=dados['registro'])
        
        cpfWithOutSymbols = remove_symbols_cpf(dados['cpf'])

        cpfIsValid = is_valid_cpf(cpfWithOutSymbols)

        cpfFormated = format_cpf(cpfWithOutSymbols)

        cpfExist = Professor.objects.filter(cpf=cpfFormated)

        if not cpfIsValid:

            messages.add_message(request, constants.ERROR, 'O CPF informado é invalido.')
            return redirect('/professores/novo')
        
        elif len(emailExist) == 1:

            messages.add_message(request, constants.ERROR, 'O email informado já foi cadastrado.')
            return redirect('/professores/novo')
        
        elif len(registroExist) == 1:

            messages.add_message(request, constants.ERROR, 'O registro informado já foi cadastrado.')
            return redirect('/professores/novo')
        
        elif len(cpfExist) == 1:

            messages.add_message(request, constants.ERROR, 'O CPF informado já foi cadastrado.')
            return redirect('/professores/novo')
        
        else:

            professor = Professor(
                nome = dados['nome'],
                cpf = cpfFormated,
                registro = dados['registro'],
                telefone = dados['telefone'],
                email = dados['email']
            )

            professor.save()

            messages.add_message(request, constants.SUCCESS, f'Professor {dados["nome"]} cadastrado com sucesso!')
            
            return redirect('/professores/novo')
    else:
        messages.add_message(request, constants.ERROR, 'Você precisa estar autenticado para acessar esta página.')
        return redirect('/')

def alterar_status_professor(request, id):

    if request.user.is_authenticated:

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
    else:
        messages.add_message(request, constants.ERROR, 'Você precisa estar autenticado para acessar esta página.')
        return redirect('/')
    
def editar_professor(request, id):

    if request.user.is_authenticated:
        
        if (request.method) == 'GET':
            try:
                professor = Professor.objects.get(id=id)
                return render(request, 'novoProfessor.html', {'edit': True, 'professor': professor})
            except Professor.DoesNotExist:
                messages.add_message(request, constants.ERROR, 'O professor informado não existe.')
                return redirect('/professores/gerenciar')
        else:
            try:
                
                professor = Professor.objects.get(id=id)

                dados = {
                    'nome': request.POST.get('nome'),
                    'cpf': request.POST.get('cpf'),
                    'registro': request.POST.get('registro'),
                    'telefone': request.POST.get('telefone'),
                    'email':request.POST.get('email')
                }

                for dado in dados:
                    if len(dados[dado].strip()) == 0:
                        messages.add_message(request, constants.ERROR, 'Preencha todos os campos.')
                        return redirect(f'/professores/editar_professor/{professor.id}')

                emailExist = Professor.objects.filter(email__iexact=dados['email'])
                registroExist = Professor.objects.filter(registro=dados['registro'])

                cpfWithOutSymbols = remove_symbols_cpf(dados['cpf'])

                cpfIsValid = is_valid_cpf(cpfWithOutSymbols)

                cpfFormated = format_cpf(cpfWithOutSymbols)

                cpfExist = Professor.objects.filter(cpf=cpfFormated)

                if not cpfIsValid:

                    messages.add_message(request, constants.ERROR, 'O CPF informado não é valido.')
                    return redirect(f'/professores/editar_professor/{professor.id}')
                
                elif emailExist and emailExist[0].id != professor.id:

                    messages.add_message(request, constants.ERROR, 'O email informado já foi cadastrado.')
                    return redirect(f'/professores/editar_professor/{professor.id}')
                
                elif registroExist and registroExist[0].id != professor.id:

                    messages.add_message(request, constants.ERROR, 'O Nº de registro informado já foi cadastrado.')
                    return redirect(f'/professores/editar_professor/{professor.id}')
                
                elif cpfExist and cpfExist[0].id != professor.id:

                    messages.add_message(request, constants.ERROR, 'O CPF informado já foi cadastrado.')
                    return redirect(f'/professores/editar_professor/{professor.id}')
                
                else:

                    professor.nome = dados['nome']
                    professor.cpf = cpfFormated
                    professor.registro = dados['registro']
                    professor.telefone = dados['telefone']
                    professor.email = dados['email']

                    professor.save()

                    messages.add_message(request, constants.SUCCESS, f'O professor {professor.nome} foi editado com sucesso.')

                    return redirect('/professores/gerenciar/')
                
            except Professor.DoesNotExist:
                messages.add_message(request, constants.ERROR, 'O professor informado não existe.')
                return redirect('/professores/gerenciar')
    else:
        messages.add_message(request, constants.ERROR, 'Você precisa estar autenticado para acessar esta página.')
        return redirect('/')
    
def detalhes_professor(request, id):
    if request.user.is_authenticated:
        try:
            professor = Professor.objects.get(id=id)

            return render(request, 'detalhes_professor.html', {'professor': professor})
        except Professor.DoesNotExist:
            messages.add_message(request, constants.ERROR, 'O professor informado não existe.')
            return redirect('/professores/gerenciar')
    else:
        messages.add_message(request, constants.ERROR, 'Você precisa estar autenticado para acessar esta página.')
        return redirect('/')