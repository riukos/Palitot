# portfolio/views.py
from django.shortcuts import render, get_object_or_404
from .models import Projeto, Imagem

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def project_list(request):
    projetos = Projeto.objects.all()
    return render(request, 'project_list.html', {'projetos': projetos})

def project_detail(request, projeto_id):
    projeto = get_object_or_404(Projeto, pk=projeto_id)
    imagens = Imagem.objects.filter(projeto=projeto)
    link_youtube = projeto.link_youtube
    youtube_id = link_youtube.split('=')[-1]

    context = {
        'projeto': projeto,
        'imagens': imagens,
        'youtube_id': youtube_id,
    }
    return render(request, 'project_detail.html', context)