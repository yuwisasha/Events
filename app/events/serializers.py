from rest_framework.serializers import ModelSerializer, StringRelatedField

from .models import Event
from organizations.serializers import RetrieveOrganizationSerializer


class EventSerializer(ModelSerializer):

    organizations = StringRelatedField(many=True)

    class Meta:
        model = Event
        fields = '__all__'


class RetrieveEventSerializer(ModelSerializer):

    organizations = RetrieveOrganizationSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = '__all__'

