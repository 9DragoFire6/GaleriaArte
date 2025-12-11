from django.contrib import admin
from .models import PerfilUsuario

@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ['user', 'tipo_usuario', 'fecha_registro']
    list_filter = ['tipo_usuario', 'fecha_registro']
    search_fields = ['user__username', 'user__email']
