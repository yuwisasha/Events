from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Organization
from users.serializers import UserSerializer


class OrganizationSeralizer(ModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"


class RetrieveOrganizationSerializer(ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    full_address = SerializerMethodField()

    def get_full_address(self, instance):
        return '{} {}'.format(instance.address, instance.postcode)

    class Meta:
        model = Organization
        fields = (
            "title",
            "description",
            "full_address",
            "users",
        )
