from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    TIPO_USUARIO_CHOICES = [
        ('administrador', 'Administrador'),
        ('espectador', 'Espectador'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES, default='espectador')
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfiles de Usuario"
    
    def __str__(self):
        return f"{self.user.username} - {self.get_tipo_usuario_display()}"
