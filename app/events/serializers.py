from rest_framework.serializers import ModelSerializer, SlugRelatedField, StringRelatedField

from .models import Event
from organizations.models import Organization
from organizations.serializers import RetrieveOrganizationSerializer


class EventSerializer(ModelSerializer):
    organizations = SlugRelatedField(
        many=True,
        # read_only=True,
        slug_field='title',
        queryset=Organization.objects.all()
    )

    class Meta:
        model = Event
        fields = "__all__"


class RetrieveEventSerializer(ModelSerializer):
    organizations = RetrieveOrganizationSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = "__all__"
