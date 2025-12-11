import requests

API_BASE_URL = "http://127.0.0.1:8000/api/tickets/"

def obtener_tickets():
    """
    Consume el método GET de la API de tickets.
    """
    try:
        response = requests.get(API_BASE_URL, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return []
