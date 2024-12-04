from rest_framework.views import APIView, Response
from esoterics.settings import BOT_TOKEN
import requests

class SetWebhookView(APIView):
  permission_classes = []
  
  def get(self, request):
    url = 'https://matrixmd.pythonanywhere.com/bot/'
    requests.post(f'https://api.telegram.org/bot{BOT_TOKEN}/setWebhook?url={url}')
    return Response('Ok')