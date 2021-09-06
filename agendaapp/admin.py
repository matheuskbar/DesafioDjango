from django.contrib import admin
from agendaapp.models.newsletter import NewsletterBD

# Register your models here.
@admin.register(NewsletterBD)

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'email',]
