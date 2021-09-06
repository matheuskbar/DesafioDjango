from django.urls import path
from . import views

app_name = 'guiaapp'

urlpatterns = [
    #/guiaapp/
    path('filmes/', views.list, name='filme_list'),
    path('filmes/create', views.create, name='filme_create'),
    path('filmes/<int:filme_id>', views.read, name='filme_read'),
    path('filmes/update/<int:filme_id>', views.update, name='filme_update'),
    path('filmes/delete/<int:filme_id>', views.delete, name='filme_delete'),
]
