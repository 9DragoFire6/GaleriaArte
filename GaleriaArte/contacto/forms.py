from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(
        label="Nombre completo",
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Tu nombre completo'})
    )
    email = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={'placeholder': 'ejemplo@correo.com'})
    )
    asunto = forms.CharField(
        label="Asunto",
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Motivo del mensaje'})
    )
    mensaje = forms.CharField(
        label="Mensaje",
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Escribe tu mensaje aquí...'})
    )

    MOTIVO_CHOICES = [
        ('compra', 'Interés en una obra'),
        ('colaboracion', 'Colaboración artística'),
        ('consulta', 'Consulta general'),
    ]
    motivo = forms.ChoiceField(
        label="Motivo del contacto",
        choices=MOTIVO_CHOICES
    )
