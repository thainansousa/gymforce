from django.db import models

class Empresa(models.Model):

    choices_status = (
        (True, 'Ativo'),
        (False, 'Inativo')
    )

    razaoSocial = models.CharField(max_length=255)
    fantasia = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=100)
    status = models.BooleanField(default=True, choices=choices_status)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.cnpj
