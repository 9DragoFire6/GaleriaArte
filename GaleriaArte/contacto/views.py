from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import ContactoForm

def contacto(request):
    form = ContactoForm()

    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            email = form.cleaned_data["email"]
            asunto = form.cleaned_data["asunto"]
            mensaje = form.cleaned_data["mensaje"]
            motivo = form.cleaned_data["motivo"]

            # Construimos el cuerpo del correo
            cuerpo = (
                f"Motivo: {motivo}\n"
                f"Nombre: {nombre}\n"
                f"Correo: {email}\n\n"
                f"Mensaje:\n{mensaje}"
            )

            # Envío del correo a través de Mailtrap
            send_mail(
                subject=asunto,
                message=cuerpo,
                from_email=email,  # remitente
                recipient_list=["destino@ejemplo.com"],  # tu correo o el que quieras
            )

            messages.success(request, "Tu mensaje fue enviado con éxito. Te responderemos pronto.")
            return redirect("contacto")  # redirige para evitar reenvío al refrescar
        else:
            messages.error(request, "Por favor corrige los errores del formulario.")

    return render(request, 'contacto/contacto.html', {'form': form})

