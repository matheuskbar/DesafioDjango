from django import forms
from agendaapp.models import NewsletterBD


class RecuperarSenhaForm(forms.ModelForm):

    class Meta:
        model = NewsletterBD
        fields = '__all__'
