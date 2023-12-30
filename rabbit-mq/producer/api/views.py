from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import send_message, get_queue

class AddMessageToQueue(APIView):
    def get(self, request):
        onQueue = get_queue()
        return Response({'status': 'success', 'messages_length_on_queue': onQueue}, status=status.HTTP_200_OK)
    
    def post(self, request):
        message = request.data.get('message')
        
        if message:
            send_message(message)
            return Response({'status': 'Message added to queue with delay'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status': 'Bad request - Message missing'}, status=status.HTTP_400_BAD_REQUEST)
