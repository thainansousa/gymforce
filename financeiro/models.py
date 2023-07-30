from django.db import models

class Mensalidade(models.Model):

    choices_status = (
        (True, 'Ativo'),
        (False, 'Inativo')
    )

    nome = models.CharField(max_length=255)
    valor = models.FloatField()
    status = models.BooleanField(default=True, choices=choices_status)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.nome
