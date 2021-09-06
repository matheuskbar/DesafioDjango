from django import forms
from agendaapp.models.newsletter import NewsletterBD

class NewsletterForm(forms.ModelForm):

    class Meta:
        model = NewsletterBD
        fields = '__all__'

    def __init__(self, *args, **kargs):
        super(NewsletterForm, self).__init__(*args, **kargs)
        for campo in self.visible_fields():
            campo.field.widget.attrs['class'] = 'form-control'