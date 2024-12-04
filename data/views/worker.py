from rest_framework.views import APIView, Response

from data.matrix import Matrix
from data.models import BlockType, Block, CodeBlock, Card

class WorkerView(APIView):
  permission_classes = []
  
  def get(self, request):
    return Response()