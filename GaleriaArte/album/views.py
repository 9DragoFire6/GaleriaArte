from django.shortcuts import render
from django.core.paginator import Paginator
from .models import ObraArte, Categoria, Artista

def album_list(request):
    categoria_id = request.GET.get('categoria')
    artista_id = request.GET.get('artista')
    tecnica = request.GET.get('tecnica')

    obras_list = ObraArte.objects.all()

    # --- Filtros activos ---
    if categoria_id and categoria_id.isdigit():
        obras_list = obras_list.filter(categoria__id=categoria_id)
    if artista_id and artista_id.isdigit():
        obras_list = obras_list.filter(artista_rel__id=artista_id)
    if tecnica and tecnica.strip():
        obras_list = obras_list.filter(tecnica__icontains=tecnica)

    paginator = Paginator(obras_list, 2)
    page_number = request.GET.get('page')
    obras = paginator.get_page(page_number)

    context = {
        'obras': obras,
        'categorias': Categoria.objects.all(),
        'artistas': Artista.objects.all(),
        'categoria_seleccionada': int(categoria_id) if categoria_id and categoria_id.isdigit() else None,
        'artista_seleccionado': int(artista_id) if artista_id and artista_id.isdigit() else None,
        'tecnica_actual': tecnica or "",
    }
    return render(request, 'album/album.html', context)
