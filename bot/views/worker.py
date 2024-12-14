from rest_framework.views import APIView, Response
from esoterics.settings import BOT_TOKEN, CHANNEL_ID, CHAT_ID
import requests

from data.models import Card
from bot.dispatcher import Dispatcher
from bot.util import PhotoReply
ROOT = f'https://api.telegram.org/bot{BOT_TOKEN}'

class WorkerView(APIView):
  permission_classes = []
  
  def get(self, request):
    return Response()