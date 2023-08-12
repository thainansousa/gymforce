import uuid
from django.db import models

class RecuperarSenha(models.Model):

    token = models.UUIDField(
        default= uuid.uuid4,
        editable= False
    )
    status = models.BooleanField(
        default= False
    )
    user_id = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.token