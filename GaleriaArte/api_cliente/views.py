from django.shortcuts import render
from .services import obtener_tickets

def lista_tickets(request):
    """
    Vista que consume el GET de la API de tickets y muestra los resultados.
    """
    tickets = obtener_tickets()  # lista de diccionarios

    total = len(tickets)
    completados = sum(1 for t in tickets if t.get('completed'))
    pendientes = total - completados

    context = {
        'tickets': tickets,
        'total': total,
        'completados': completados,
        'pendientes': pendientes,
    }
    return render(request, 'api_cliente/lista_tickets.html', context)
