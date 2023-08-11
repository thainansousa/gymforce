from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    choices_status = (
        (True, 'Ativo'),
        (False, 'Inativo')
    )
    choices_nivel_adm = (
        (True, 'Administrador'),
        (False, 'Usuario')
    )

    is_staff = models.BooleanField(
        ("staff status"),
        default=False,
        choices=choices_nivel_adm
    )
    is_active = models.BooleanField(
        ("active"),
        default=True,
        choices=choices_status
    )

    cpf = models.CharField(max_length=30, null=False, blank=False, default="")
    telefone = models.CharField(max_length=30, null=False, blank=False, default="")

    def __str__(self):
        return self.username