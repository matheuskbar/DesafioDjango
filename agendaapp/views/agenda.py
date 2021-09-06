from django.shortcuts import render, redirect, get_object_or_404
from agendaapp.forms.newsletter import NewsletterForm


def em_producao(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewsletterForm()
    context = {
        'nome': 'App em produção',
        'form': form,
    }
    return render(request, 'em_producao.html', context)