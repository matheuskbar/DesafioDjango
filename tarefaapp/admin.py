from django.contrib import admin
from tarefaapp.models.tarefa import TarefaBD

# Register your models here.
@admin.register(TarefaBD)

class TarefaAdmin(admin.ModelAdmin):
    list_display = ['id', 'conteudo', 'data',]
