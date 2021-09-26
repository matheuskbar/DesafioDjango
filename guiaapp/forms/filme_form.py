from django import forms
from guiaapp.models import Filme


# Exemplo de formulário que será persistido no banco de dados
class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = '__all__' # Também pode ser uma lista dos campos
        exclude = ['usuario'] # Campos a serem exluidos do formulário

    # def __init__(self, *args, **kwargs):
    #     super(FilmeForm, self).__init__(*args, **kwargs)
    #     for new_field in self.visible_fields():
    #         new_field.field.widget.attrs['class'] = 'form-control'
