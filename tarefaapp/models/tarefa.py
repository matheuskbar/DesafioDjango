from django.db import models
from django.contrib.auth.models import User


class TarefaBD(models.Model):
    conteudo = models.CharField(max_length=1000)
    data = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = False

    def __str__(self):
        return str(self.id)
