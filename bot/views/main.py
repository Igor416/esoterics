from rest_framework.views import APIView, Response

from bot.util import Update
from bot.dispatcher import Dispatcher

class MainView(APIView):
  permission_classes = []
  
  def post(self, request):
    update = Update(**request.data)
    Dispatcher.dispatch(update)
    return Response('Ok')