from django.shortcuts import render, redirect

from .models import Mensalidade

from django.contrib.messages import constants
from django.contrib import messages

def novo(request):
    
    if request.user.is_authenticated:
        return render(request, 'nova_mensalidade.html')
    else:
        messages.add_message(request, constants.ERROR, 'Você precisa estar autenticado para acessar esta página.')
        return redirect('/')

def gerenciar(request):

    if request.user.is_authenticated:
        nome = request.GET.get('plano')

        if nome:
            mensalidades = Mensalidade.objects.filter(nome__iexact=nome).order_by('-id')
        else:
            mensalidades = Mensalidade.objects.all().order_by('-id')
        return render(request, 'gerenciar_mensalidades.html', {'edit': False, 'mensalidades': mensalidades})
    else:
        messages.add_message(request, constants.ERROR, 'Você precisa estar autenticado para acessar esta página.')
        return redirect('/')

def cadastrar_mensalidade(request):

    if request.user.is_authenticated:
    
        dados = {
            'nome_do_plano': request.POST.get('plano'),
            'valor': request.POST.get('valor')
        }

        for dado in dados:
            if len(dados[dado].strip()) == 0:
                messages.add_message(request, constants.ERROR, 'Preencha todos os campos!')
                return redirect('/financeiro/novo')

        planoExist = Mensalidade.objects.filter(nome=dados['nome_do_plano'])

        if len(planoExist) == 1:
            messages.add_message(request, constants.ERROR, 'Esse plano já foi cadastrado.')
            return redirect('/financeiro/novo')


        mensalidade = Mensalidade(
            nome = dados['nome_do_plano'],
            valor = dados['valor']
        )

        mensalidade.save()
            
        messages.add_message(request, constants.SUCCESS, f'Mensalidade {dados["nome_do_plano"]} cadastrada com sucesso!')

        return redirect('/financeiro/novo')
    
    else:
        messages.add_message(request, constants.ERROR, 'Você precisa estar autenticado para acessar esta página.')
        return redirect('/')

def alterar_status_mensalidade(request, id):

    if request.user.is_authenticated:

        try:

            mensalidade = Mensalidade.objects.get(id=id)

            mensalidade.status = not mensalidade.status

            mensalidade.save()


            if mensalidade.status:
                messages.add_message(request, constants.SUCCESS, f'A mensalidade {mensalidade.nome} foi ativada com sucesso!')
            else:
                messages.add_message(request, constants.SUCCESS, f'A mensalidade {mensalidade.nome} foi inativada com sucesso!')

        except Mensalidade.DoesNotExist:
            messages.add_message(request, constants.ERROR, "A mensalidade informada não existe!")
        
        return redirect('/financeiro/gerenciar')
    else:
        messages.add_message(request, constants.ERROR, 'Você precisa estar autenticado para acessar esta página.')
        return redirect('/')
    
def editar_plano_mensalidade(request, id):

    if request.user.is_authenticated:

        if (request.method) == 'GET':
            try:

                planoMensalidade = Mensalidade.objects.get(id=id)
                return render(request, 'nova_mensalidade.html', {'edit': True, 'mensalidade': planoMensalidade})
            except Mensalidade.DoesNotExist:
                messages.add_message(request, constants.ERROR, 'Plano de mensalidade não encontrado.')
                return redirect('/financeiro/gerenciar')
        else:
            try:

                planoMensalidade = Mensalidade.objects.get(id=id)

                dados = {
                    'plano': request.POST.get('plano'),
                    'valor': request.POST.get('valor')
                }

                planoExist = Mensalidade.objects.filter(nome__iexact=dados['plano'])

                if planoExist:
                    if not planoExist[0].id == planoMensalidade.id:
                        messages.add_message(request, constants.ERROR, 'Esse plano já foi cadastrado.')
                        return redirect(f'/financeiro/editar_plano_mensalidade/{planoMensalidade.id}')

                valorFormatado = dados['valor'].replace(',','.')
            
                for dado in dados:
                    if len(dado.strip()) == 0:
                        messages.add_message(request, constants.ERROR, 'Preencha todos os campos.')
                        return redirect(f'/financeiro/editar_plano_mensalidade/{planoMensalidade.id}')

            
                planoMensalidade.nome = dados['plano']
                planoMensalidade.valor = valorFormatado


                planoMensalidade.save()

                messages.add_message(request, constants.SUCCESS, f'O {planoMensalidade.nome} foi editado com sucesso.')
                return redirect('/financeiro/gerenciar')
        
            except Mensalidade.DoesNotExist:
                messages.add_message(request, constants.ERROR, 'Plano de mensalidade não encontrado.')
                return redirect('/financeiro/gerenciar')