import json
from django.dispatch import receiver
from channels.generic.websocket import AsyncwebsocketConsumer

class ChatConsumer(AsyncwebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'Test-Room'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, closee_code):
        await self.channel_layer.group_discard(
        self.room_group_name,
        self.channel_name
    )
    print('Disconnected!')

    async def receive(self, dict_data):
        receive_dict = json.loads(dict_data)
        message = receive_dict['message']
        action = receive_dict['action']

        if (action == 'new-offer') or (action == 'new-answer'):
            receiver_channel_name = receive_dict['message']['recevier_channel_name']
            receive_dict['message']['receiver_channel_name'] = self.channel_name
            
            await self.channel_layer.send(
                receiver_channel_name,
                {
                    'type':'send.message',
                    'receive_dict': receive_dict
                }
            )
            
            return

        receive_dict['message']['receiver_channel_name'] = self.channel_name

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'send.message',
                'receive_dict': receive_dict
            }
        )

    async def send_message(self, event):
        receive_dict = event['receive_dict']

        await self.send(text_data=json.dumps(receive_dict))