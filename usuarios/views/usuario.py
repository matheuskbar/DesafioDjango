#from django.urls import reverse_lazy
#from django.views.generic.edit import CreateView
from django.shortcuts import redirect, render, get_object_or_404

from usuarios.forms import UsuarioForm
from usuarios.models import Perfil
from usuarios.forms import PerfilForm

# Aqui é a forma atraves de uma view generica
#class UsuarioCreate(CreateView):
#    template_name = 'usuarios/login.html'
#    form_class = UsuarioForm
#    success_url = reverse_lazy('login')

#Aqui é por função, como o restante do projeto
def usuario_create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            Perfil.objects.create(usuario=form.instance)
            # TODO: Implementar mensagem
            return redirect('login')
    else:
        form = UsuarioForm()

    context = {
        'form': form,
    }

    return render(request, 'usuarios/cadastrar.html', context) # Poderia usar o mesmo template do login, com algumas modificações no html

def usuario_update(request):
    perfil = get_object_or_404(Perfil, usuario=request.user)
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PerfilForm(instance=perfil)
    context = {
        'form': form,
    }
    return render(request, 'usuarios/perfil.html', context)




