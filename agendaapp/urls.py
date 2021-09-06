from django.urls import path
from agendaapp import views

urlpatterns = [
    # /agendaapp/
    path('agenda/', views.em_producao, name='em_producao'),
]
