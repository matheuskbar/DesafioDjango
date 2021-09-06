from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    nome_completo = models.CharField(max_length=150, null=True, verbose_name='Nome Completo', help_text='Digite seu nome completo.')
    email = models.EmailField(max_length=200, blank=True, verbose_name='E-mail', help_text='Digite seu e-mail.')
    cpf = models.CharField(max_length=14, blank=True, verbose_name='CPF', help_text='Digite seu número de CPF (opcional)')
    telefone = models.CharField(max_length=14, null=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

