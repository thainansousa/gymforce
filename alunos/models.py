from django.db import models

from financeiro.models import Mensalidade

class Aluno(models.Model):

    choices_status = (
        (True, 'Ativo'),
        (False, 'Inativo')
    )
    
    nome = models.CharField(max_length=255)
    rg = models.CharField(max_length=25)
    cpf = models.CharField(max_length=25)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=25)
    email = models.CharField(max_length=255)
    mensalidade = models.ForeignKey(Mensalidade, on_delete=models.DO_NOTHING)
    status = models.BooleanField(default=True, choices=choices_status)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email