from rest_framework.views import APIView, Response

from user.serializers import MasterSerializer
from user.models import Master

class MastersView(APIView):
  permission_classes = []
  
  def get(self, request, name):
    if name != 'all':
      queryset = Master.objects.get(name=name)
      serializer = MasterSerializer(queryset)
    else:
      queryset = Master.objects.all()
      serializer = MasterSerializer(queryset, many=True)
    return Response(serializer.data)