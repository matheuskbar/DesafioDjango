from django.urls import path
from tarefaapp import views

urlpatterns = [
    # /tarefaapp/
    path('tarefa/', views.index, name='tarefa_index'),
    path('tarefa/read/<int:id>', views.read, name='tarefa_read'),
    path('tarefa/update/<int:id>', views.update, name='tarefa_update'),
    path('tarefa/delete/<int:id>', views.delete, name='tarefa_delete'),
]