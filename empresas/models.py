from django.db import models

class Empresa(models.Model):

    razaoSocial = models.CharField(max_length=255)
    fantasia = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.cnpj
