import json
from channels.generic.websocket import AsyncWebsocketConsumer

class SheetConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.sheet_id = self.scope['url_route']['kwargs']['sheet_id']
        self.sheet_group_name = f'sheet_{self.sheet_id}'

        # Join sheet group
        await self.channel_layer.group_add(
            self.sheet_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave sheet group
        await self.channel_layer.group_discard(
            self.sheet_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to sheet group
        await self.channel_layer.group_send(
            self.sheet_group_name,
            {
                'type': 'sheet_message',
                'message': message
            }
        )

    # Receive message from sheet group
    async def sheet_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
