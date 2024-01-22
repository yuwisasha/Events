from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

from .serializers import ConversationListSerializer, ConversationSerializer
from .models import Conversation
from users.models import User


class CreateRetrieveConversationView(CreateAPIView, RetrieveAPIView):
    serializer_class = ConversationSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        email = data.pop("email")
        try:
            participant = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {"message": "You cannot chat with a non existent user"},
                status=status.HTTP_404_NOT_FOUND,
            )

        try:
            conversation = Conversation.objects.get(
                Q(initiator=request.user, receiver=participant)
                | Q(initiator=participant, receiver=request.user)
            )

        except conversation.DoesNotExist:
            conversation = Conversation.objects.create(
                initiator=request.user, receiver=participant
            )

        return Response(
            self.serializer_class(conversation).data,
            status=status.HTTP_200_OK,
        )

    def get(self, request, convo_id, *args, **kwargs):
        conversation = Conversation.objects.get(
            Q(initiator=request.user)
            | Q(receiver=request.user)
            | Q(id=convo_id)
        )

        return Response(self.serializer_class(conversation).data, status=status.HTTP_200_OK)


class ListConversationsView(ListAPIView):
    serializer_class = ConversationListSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def list(self, request, *args, **kwargs):
        conversations = Conversation.objects.filter(
            Q(initiator=request.user) | Q(receiver=request.user)
        )
        print(self.serializer_class(conversations, many=True).data)
        return Response(
            self.serializer_class(conversations, many=True).data,
            status=status.HTTP_200_OK,
        )
