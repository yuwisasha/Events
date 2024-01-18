from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Organization
from .serializers import OrganizationSeralizer, RetrieveOrganizationSerializer


class CreateOrganizationView(CreateAPIView):

    model = Organization
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = OrganizationSeralizer


class RetrieveOrganizationView(RetrieveAPIView):

    model = Organization
    permission_classes = [
        IsAuthenticated,
    ]
    queryset = Organization.objects.all()
    serializer_class = RetrieveOrganizationSerializer