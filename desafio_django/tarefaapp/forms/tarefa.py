from django import forms
from tarefaapp.models.tarefa import TarefaBD

class ConteudoForm(forms.ModelForm):

    class Meta:
        model = TarefaBD
        fields = ['conteudo',]