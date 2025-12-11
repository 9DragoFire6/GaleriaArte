from django.contrib import admin
from django.urls import path, re_path, include   
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from core import views as views_core
from album import views as views_album

urlpatterns = [
    path('', views_core.index, name="index"),
    path('album/', views_album.album_list, name="album"),
    path('info/', views_core.info, name="info"),
    path('preguntas/', views_core.preguntas, name="preguntas"),
    path('contacto/', include('contacto.urls')), 
    path('usuarios/', include('usuarios.urls')),
    path('admin/', admin.site.urls),
    path('api-cliente/', include('api_cliente.urls')),
]

handler404 = 'core.views.custom_404'

if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]
else:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
