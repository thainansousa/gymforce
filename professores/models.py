from django.db import models

class Professor(models.Model):

    choices_status = (
        (True, 'Ativo'),
        (False, 'Inativo')
    )

    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telefone = models.CharField(max_length=25)
    cpf = models.CharField(max_length=25)
    registro = models.CharField(max_length=50)
    status = models.BooleanField(default=True, choices=choices_status)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.email
