from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Ticket
from .serializers import TicketSerializer

@api_view(['GET', 'POST'])
def ticket_list(request):
    # GET: listar tickets
    if request.method == 'GET':
        tickets = Ticket.objects.all().order_by('-timestamp')
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)

    # POST: crear ticket
    elif request.method == 'POST':
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
