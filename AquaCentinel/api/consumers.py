import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = self.room_name

        # Unir al grupo de la sala
        print(f'Uniendo usuario a la room {self.room_group_name}')
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Salir del grupo
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def send_new_data(self, event):
        # Envía el mensaje recibido desde la vista al WebSocket
        await self.send(text_data=json.dumps(event['data']))




# Esto puede servir después...
# await self.channel_layer.group_send(
#     "nombre_del_grupo", # room
#     {
#         "type": "chat.message", # Nombre del método que manejará el evento
#         "message": "Hola a todos",
#     }
# )