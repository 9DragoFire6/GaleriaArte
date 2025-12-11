from django.db import models

# Modelo Artista
class Artista(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre del Artista")
    pais = models.CharField(max_length=100, verbose_name="País de Origen", blank=True, null=True)
    biografia = models.TextField(verbose_name="Biografía", blank=True, null=True)

    class Meta:
        verbose_name = "Artista"
        verbose_name_plural = "Artistas"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


# Modelo Categoría
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Categoría")
    descripcion = models.TextField(verbose_name="Descripción", blank=True, null=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


# Modelo Obra de Arte (relacionado con Artista y Categoría)
class ObraArte(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    artista = models.CharField(max_length=150, verbose_name="Artista (texto)", blank=True, null=True)
    artista_rel = models.ForeignKey(Artista, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Artista (relación)")
    year = models.CharField(max_length=50, verbose_name="Año", blank=True, null=True)
    tecnica = models.CharField(max_length=200, verbose_name="Técnica")
    dimensiones = models.CharField(max_length=100, verbose_name="Dimensiones")
    descripcion = models.TextField(verbose_name="Descripción")
    imagen = models.ImageField(upload_to="obras/", verbose_name="Imagen de la Obra", blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Categoría")
    likes = models.IntegerField(default=0, verbose_name="Likes")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Obra de Arte"
        verbose_name_plural = "Obras de Arte"
        ordering = ['-created']

    def __str__(self):
        return f"{self.titulo} - {self.artista_rel or self.artista}"
