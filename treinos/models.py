from django.db import models

from alunos.models import Aluno

class Treino(models.Model):
    nome = models.CharField(max_length=80)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __self__(self):
        return self.nome
    

class Treino_Aluno(models.Model):

    choice_diasDaSemana = (
        ('SEG', 'SEGUNDA'),
        ('TER', 'TERÇA'),
        ('QUA', 'QUARTA'),
        ('QUI', 'QUINTA'),
        ('SEX', 'SEXTA'),
        ('SAB', 'SÁBADO'),
        ('DOM', 'DOMINGO'),
    )

    choices_status = (
        (True, 'Ativo'),
        (False, 'Inativo')
    )

    treino = models.ForeignKey(Treino, on_delete=models.DO_NOTHING)
    treino_series = models.IntegerField(default=0)
    treino_qtd = models.IntegerField(default=0)
    treino_dia = models.CharField(max_length=3, choices=choice_diasDaSemana)
    aluno = models.ForeignKey(Aluno, on_delete=models.DO_NOTHING)
    status = models.BooleanField(default=True, choices=choices_status)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.aluno