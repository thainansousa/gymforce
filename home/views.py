from django.shortcuts import render

from alunos.models import Aluno

def home(request):

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
