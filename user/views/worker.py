from rest_framework.views import APIView, Response

from user.models import User, MatrixRequest

class WorkerView(APIView):
  permission_classes = []
  
  def get(self, request):
    return Response(None)
