from django.db import models

class Usuario(models.Model):

    choices_nivel_adm = (
        ('1', 'Normal'),
        ('2', 'Administrador'),
    )

    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    telefone = models.CharField(max_length=25)
    cpf = models.CharField(max_length=25)
    nivel_administrativo = models.CharField(max_length=1, choices=choices_nivel_adm)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __self__(self):
        return self.email

