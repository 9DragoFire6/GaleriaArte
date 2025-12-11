from django.shortcuts import render
from .models import CuriosidadesDeLasObras

def index(request):
    curiosidades = CuriosidadesDeLasObras.objects.all().order_by('-fecha_publicacion')
    return render(request, 'core/index.html', {'curiosidades': curiosidades})

def info(request):
    return render(request, 'core/info.html')

def preguntas(request):
    return render(request, 'core/preguntas.html')

def custom_404(request, exception):
    context = {'error_message': 'Obra no encontrada :('}
    return render(request, 'core/404.html', context, status=404)
