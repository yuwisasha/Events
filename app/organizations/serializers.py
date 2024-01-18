from rest_framework.serializers import ModelSerializer

from .models import Organization
from users.serializers import UserSerializer

class OrganizationSeralizer(ModelSerializer):

    class Meta:
        model = Organization
        fields = '__all__'


class RetrieveOrganizationSerializer(ModelSerializer):

    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Organization
        fields = (
            'title',
            'description',
            'address',
            'postcode',
            'users',
        )

