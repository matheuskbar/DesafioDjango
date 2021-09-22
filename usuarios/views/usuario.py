#from django.urls import reverse_lazy
#from django.views.generic.edit import CreateView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from django.core.mail import send_mail
from usuarios.forms import UsuarioForm
from usuarios.models import Perfil
from usuarios.forms import PerfilForm
from usuarios.gerador_senha import *


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

def usuario_read(request):
    usuario = get_object_or_404(Perfil, usuario=request.user)
    context = {
        'usuario': usuario,
    }
    return render(request, 'usuarios/perfil.html', context)

def usuario_update(request):
    perfil = get_object_or_404(Perfil, usuario=request.user)
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('meus_dados')
    else:
        form = PerfilForm(instance=perfil)
    context = {
        'form': form,
    }
    return render(request, 'usuarios/perfil_update.html', context)

def alterar_senha(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {
        'form': form
    }
    return render(request, 'usuarios/alterar_senha.html', context)


def recuperar_senha(request):
    if request.method == 'POST':
        nome = request.POST.get('nome_usuario')
        email = request.POST.get('email_rec_senha')
        nova_senha = gerador_senha() # Gera uma nova senha aleatória

        # Trocar senha do usuário
        usuario = User.objects.get(username=nome)
        usuario.set_password(nova_senha)
        usuario.save()

        mensagem = f'''
        Olá {nome}, foi gerada uma nova senha para seu acesso.
        Já poderá acessar o painel com seu nome de usuário e sua nova senha.
        
        
        Nome de Usuário: {nome}
        Nova Senha: {nova_senha}

        Obs.: Após o login, poderá alterar a senha em seu perfil.
        
        Att., Equipe
        '''
        send_mail(
            'Recuperar Senha',
            mensagem,
            email,
            ['matheuskbar@gmail.com'],
            fail_silently = False
        )
        return redirect('login')
    return render(request, 'usuarios/recuperar_senha.html')




