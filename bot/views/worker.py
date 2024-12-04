from rest_framework.views import APIView, Response

from bot.models import Prediction
from data.models import Card

class WorkerView(APIView):
  permission_classes = []
  
  def get(self, request):
    return Response()