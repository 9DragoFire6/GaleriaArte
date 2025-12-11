from django.urls import path
from .views import lista_tickets

urlpatterns = [
    path('tickets/', lista_tickets, name='tickets_api_cliente'),
]
