from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = [
            'id',
            'task',
            'timestamp',
            'completed',
            'updated',
            'user',
        ]
