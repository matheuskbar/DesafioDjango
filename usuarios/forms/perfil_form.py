from django import forms
from django.forms.widgets import ClearableFileInput
from usuarios.models import Perfil


# Exemplo de formulário que será persistido no banco de dados
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = '__all__' # Também pode ser uma lista dos campos
        exclude = ['usuario'] # Campos a serem exluidos do formulário

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})
        self.fields['telefone'].widget.attrs.update({'class': 'mask-tel'})
