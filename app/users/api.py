from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model

from .serializers import CreateUserSerializer, UserSerializer
from .models import User


class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        AllowAny,
    ]
    serializer_class = CreateUserSerializer
