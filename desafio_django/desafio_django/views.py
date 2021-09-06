from django.shortcuts import render


def index(request):
    context = {
        'nome': 'Matheus'
    }
    return render(request, 'conteudo.html', context)
