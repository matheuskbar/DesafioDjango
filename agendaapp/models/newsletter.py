from django.db import models


class NewsletterBD(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome Completo')
    email = models.EmailField(max_length=100, verbose_name='E-mail')

    class Meta:
        abstract: False

    def __str__(self):
        return str(self.id)
