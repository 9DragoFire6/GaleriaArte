from django import forms
from .models import ObraDeArte

class ObraDeArteForm(forms.ModelForm):
    class Meta:
        model = ObraDeArte
        fields = ['titulo', 'artista', 'año', 'tecnica', 'dimensiones', 'descripcion', 'imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Título de la obra'}),
            'artista': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Nombre del artista'}),
            'año': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Año de creación'}),
            'tecnica': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Técnica utilizada'}),
            'dimensiones': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Dimensiones de la obra'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 5, 'placeholder': 'Descripción detallada'}),
            'imagen': forms.FileInput(attrs={'class': 'form-file'}),
        }