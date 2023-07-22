from django.db import models

class Mensalidade(models.Model):
    nome = models.CharField(max_length=255)
    valor = models.FloatField()
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.nome
