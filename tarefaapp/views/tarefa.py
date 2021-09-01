from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from tarefaapp.models.tarefa import TarefaBD
from tarefaapp.forms.tarefa import ConteudoForm
from django.contrib.auth.decorators import login_required


@login_required(login_url=reverse_lazy('login'))
def index(request):
    tarefas = TarefaBD.objects.filter(usuario=request.user)
    if request.method == 'POST':
        form = ConteudoForm(request.POST)
        form.instance.usuario = request.user
        if form.is_valid():
            form.save()
            return redirect('tarefa_index')
    else:
        form = ConteudoForm()
        context = {
            'form': form,
        }
        render(request, 'tarefa_index.html', context)
    context = {
        'tarefas': tarefas,
        'form': form,
    }
    return render(request, 'tarefa_index.html', context)


@login_required(login_url=reverse_lazy('login'))
def read(request, id):
    tarefa = get_object_or_404(TarefaBD, pk=id, usuario=request.user)
    context = {
        'tarefa': tarefa
    }
    return render(request, 'tarefa_read.html', context)


@login_required(login_url=reverse_lazy('login'))
def update(request, id):
    tarefa = get_object_or_404(TarefaBD, pk=id, usuario=request.user)
    try:
        if request.method == 'POST':
            form = ConteudoForm(request.POST, instance=tarefa)
            if form.is_valid():
                form.save()
                return redirect('tarefa_index')
        else:
            form = ConteudoForm(instance=tarefa)
            context = {
                'form': form,
            }
            return render(request, 'tarefa_update.html', context)
    except:
        # TODO: mensagem
        context = {
        }
        return render(request, 'tarefa_index.html', context)


@login_required(login_url=reverse_lazy('login'))
def delete(request, id):
    tarefa = get_object_or_404(TarefaBD, pk=id, usuario=request.user)
    try:
        tarefa.delete()
        # TODO: mensagem
        return redirect('tarefa_index')
    except:
        # TODO: mensagem
        context = {
        }
        return render(request, 'tarefa_index.html', context)
