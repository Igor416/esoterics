from rest_framework.views import APIView, Response

class WorkerView(APIView):
  permission_classes = []
  
  def get(self, request):
    return Response()