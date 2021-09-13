from django import forms
from django.forms.widgets import ClearableFileInput
from usuarios.models import Perfil


# Exemplo de formulário que será persistido no banco de dados
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = '__all__' # Também pode ser uma lista dos campos
        exclude = ['usuario'] # Campos a serem exluidos do formulário