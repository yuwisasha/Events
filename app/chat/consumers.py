import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncJsonWebsocketConsumer

from .models import Message, Conversation
from .serializers import MessageSerializer


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    async def receive_json(self, content):
        message = content["message"]

        conversation = await Conversation.objects.aget(id=int(self.room_name))
        sender = self.scope["user"]

        _message = await Message.objects.acreate(
                sender=sender,
                text=message,
                conversation_id=conversation,
            )
        
        chat_type = {"type": "chat_message"}
        message_serializer = (dict(MessageSerializer(instance=_message).data))
        return_dict = {**chat_type, **message_serializer}

        await self.channel_layer.group_send(
            self.room_group_name,
            return_dict,
        )

    async def chat_message(self, event):
        dict_to_be_sent = event.copy()
        dict_to_be_sent.pop("type")
        print(dict_to_be_sent)

        await self.send_json(
                dict_to_be_sent
            )
