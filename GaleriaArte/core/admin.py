from django.contrib import admin
from .models import Noticia, CuriosidadesDeLasObras

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'created', 'updated')
    search_fields = ('titulo',)
    list_filter = ('created',)

@admin.register(CuriosidadesDeLasObras)
class CuriosidadesAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicacion')
    search_fields = ('titulo', 'autor')
    list_filter = ('fecha_publicacion',)
