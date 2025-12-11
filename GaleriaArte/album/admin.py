from django.contrib import admin
from .models import ObraArte, Artista, Categoria

# --- Admin de Artista ---
@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais')
    search_fields = ('nombre', 'pais')


# --- Admin de Categoría ---
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)


# --- Admin de ObraArte ---
@admin.register(ObraArte)
class ObraArteAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'artista_rel', 'categoria', 'year', 'likes', 'created')
    search_fields = ('titulo', 'artista', 'artista_rel__nombre')
    list_filter = ('categoria', 'artista_rel', 'year', 'created')
    readonly_fields = ('created', 'updated')
