from django.utils import timezone
from django.core.cache import cache
from django.db.models import Sum
from album.models import ObraArte

def site_info(request):
    """
    Procesador de contexto que proporciona información global para la galería:
    - site_title, site_tagline: metadatos estáticos del sitio
    - total_artworks: número total de objetos ObraArte
    - total_likes: suma de los "me gusta" en todas las obras
    - top_artworks: lista (hasta 5) de las obras más valoradas (id, título, artista, likes, imagen)
    - recent_artworks: lista (hasta 3) de las obras añadidas más recientemente (id, título, artista, imagen)
    - current_year: año actual para mostrar en el pie de página
    Almacena en caché los datos calculados durante 5 minutos para reducir la carga en la base de datos.
    """
    data = cache.get('site_info')
    if data is None:
        total_artworks = ObraArte.objects.count()
        total_likes = ObraArte.objects.aggregate(total=Sum('likes'))['total'] or 0
        top_qs = ObraArte.objects.order_by('-likes')[:5]
        recent_qs = ObraArte.objects.order_by('-created')[:3]

        # Use values to avoid heavy model instances in the template context
        top_artworks = list(top_qs.values('id','titulo','artista','likes','imagen'))
        recent_artworks = list(recent_qs.values('id','titulo','artista','imagen'))

        data = {
            'site_title': 'Galería Digital - Atenart',
            'site_tagline': 'Exposición virtual de obras de arte y patrimonio cultural',
            'total_artworks': total_artworks,
            'total_likes': total_likes,
            'top_artworks': top_artworks,
            'recent_artworks': recent_artworks,
            'current_year': timezone.now().year,
        }
        cache.set('site_info', data, 300)  # cache 5 minutes
    return data
