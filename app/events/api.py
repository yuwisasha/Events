from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
 
from .models import Event
from .serializers import EventSerializer, RetrieveEventSerializer


class CreateEventView(CreateAPIView):

    model = Event
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = EventSerializer


class RetrieveEventView(RetrieveAPIView):

    model = Event
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = Event.objects.all()
    serializer_class = RetrieveEventSerializer


class ListEventView(ListAPIView):

    model = Event
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [
        SearchFilter,
        OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = {
        "date": ['gte', 'lte'],
    }
    search_fields = ['title',]
    ordering_fields = ['date',]
    pagination_class = LimitOffsetPagination
