from django.shortcuts import render, redirect

from alunos.models import Aluno

from django.contrib.messages import constants
from django.contrib import messages

def home(request):

    if request.user.is_authenticated:
        alunos = Aluno.objects.all()

        alunosAtivos = Aluno.objects.filter(status=True)

        mensalidadesTotal = 0

        for aluno in alunos:
            if aluno.status == True:
                mensalidadesTotal += aluno.mensalidade.valor

        return render(request, 'home.html', {
            'mensalidadesTotal': mensalidadesTotal, 
            'alunosTotal': len(alunos),
            'alunosAtivos': len(alunosAtivos)})
    else:
        messages.add_message(request, constants.ERROR, 'Vocẽ precisa estar autenticado para acessar esta página.')
        return redirect('/')
