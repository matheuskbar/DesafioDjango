from guiaapp.models.base import BaseModel
from django.db import models
from django.contrib.auth.models import User


class Filme(BaseModel):
    nome = models.CharField(max_length=50, verbose_name='Nome do filme/série')
    resenha = models.CharField(max_length=100, verbose_name='Resenha')
    finalizado = models.BooleanField(verbose_name='Finalizado')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = False

    def __str__(self):
        return f'{self.nome}: {self.resenha}. Finalizado: {self.get_finalizado()}'

    def get_finalizado(self):
        if self.finalizado:
            return 'Sim'
        else:
            return 'Não'
