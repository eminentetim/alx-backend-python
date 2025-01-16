# chats/filters.py

from django_filters import rest_framework as filters
from .models import Message

class MessageFilter(filters.FilterSet):
    sender = filters.CharFilter(field_name="sender__username", lookup_expr='icontains')
    conversation = filters.CharFilter(field_name="conversation__id", lookup_expr='exact')
    start_date = filters.DateTimeFilter(field_name="sent_at", lookup_expr='gte')
    end_date = filters.DateTimeFilter(field_name="sent_at", lookup_expr='lte')

    class Meta:
        model = Message
        fields = ['sender', 'conversation', 'start_date', 'end_date']
