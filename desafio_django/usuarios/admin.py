from django.contrib import admin
from usuarios.models.perfil import Perfil

# Register your models here.
@admin.register(Perfil)

class PerfilAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome_completo', 'usuario']