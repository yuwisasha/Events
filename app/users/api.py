from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView
from django.contrib.auth import get_user_model

from .serializers import CreateUserSerializer, UserSerializer
from .models import User


class CreateUserView(CreateAPIView):
    permission_classes = [
        AllowAny,
    ]
    serializer_class = CreateUserSerializer


class ListUserView(ListAPIView):
    model = get_user_model()
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = UserSerializer
    queryset = model.objects.all()
