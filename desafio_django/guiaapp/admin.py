from django.contrib import admin
from guiaapp.models.filme import Filme

# Register your models here.
@admin.register(Filme)

class FilmeAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'finalizado', 'resenha']