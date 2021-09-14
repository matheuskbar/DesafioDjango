from django.db import models
from django.contrib.auth.models import User
from stdimage.models import StdImageField
from django.db.models import signals
from django.template.defaultfilters import slugify

class Perfil(models.Model):
    nome_completo = models.CharField(max_length=150, null=True, verbose_name='Nome Completo', help_text='Digite seu nome completo.')
    email = models.EmailField(max_length=200, blank=True, verbose_name='E-mail', help_text='Digite seu e-mail.')
    cpf = models.CharField(max_length=14, blank=True, verbose_name='CPF', help_text='Digite seu número de CPF (opcional)')
    telefone = models.CharField(max_length=14, null=True)
    foto = StdImageField('Foto de Perfil', upload_to='imagens', variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)


def perfil_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome_completo)

signals.pre_save.connect(perfil_pre_save, sender=Perfil)

