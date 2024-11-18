from rest_framework.views import APIView, Response
import json

from data.matrix import Matrix
from data.models import Category, BlockType, Block, PrevLife, Scenario
  
class WorkerView(APIView):
  permission_classes = []
  
  def get(self, request):
    return Response()