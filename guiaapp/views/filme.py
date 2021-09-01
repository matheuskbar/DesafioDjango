from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from guiaapp.models.filme import Filme
from guiaapp.forms.filme_form import FilmeForm

from django.contrib.auth.decorators import login_required



@login_required(login_url=reverse_lazy('login'))
def list(request):
    filmes = Filme.objects.filter(usuario = request.user)
    context = {
        'filmes': filmes,
    }
    return render(request, 'guiaapp/filme_list.html', context)

@login_required(login_url=reverse_lazy('login'))
def create(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST)
        form.instance.usuario = request.user
        if form.is_valid():
            form.save()
            # TODO: Implementar mensagem
            return redirect('guiaapp:filme_list')
    else:
        form = FilmeForm()
    context = {
        'form': form,
    }
    return render(request, 'guiaapp/filme_create.html', context)

@login_required(login_url=reverse_lazy('login'))
def read(request, filme_id):
    filmes = get_object_or_404(Filme, pk=filme_id, usuario=request.user)
    context = {
        'filmes': filmes
    }
    return render(request, 'guiaapp/filme_read.html', context)

@login_required(login_url=reverse_lazy('login'))
def delete(request, filme_id):
    filmes = get_object_or_404(Filme, pk=filme_id, usuario=request.user)
    try:
        filmes.delete()
        return redirect('guiaapp:filme_list')
    except:
        context = {
        }
        return render(request, 'guiaapp/filme_list.html', context)

@login_required(login_url=reverse_lazy('login'))
def update(request, filme_id):
    filmes = get_object_or_404(Filme, pk=filme_id, usuario=request.user)
    try:
        if request.method == 'POST':
            form = FilmeForm(request.POST, instance=filmes)
            if form.is_valid():
                form.save()
                # TODO: Implementar mensagem
                return redirect('guiaapp:filme_list')
        else:
            form = FilmeForm(instance=filmes)
            context = {
                'form': form,
                'filme_id': filme_id,
            }
            return render(request, 'guiaapp/filme_edit.html', context)
    except:
        # TODO: Implementar mensagem
        return redirect(request, 'guiaapp:filme_list')
