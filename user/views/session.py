from rest_framework.views import APIView, Response

from user.serializers import SessionSerializer
from user.models import Session

class SessionsView(APIView):
  def get(self, request):
    queryset = Session.objects.filter(customer=request.user)
    serializer = SessionSerializer(queryset, many=True)
    return Response(serializer.data)
  
  
  def post(self, request):
    master = request.data.pop('master')
    serializer = SessionSerializer(data={**request.data, 'master': master.get('id'), 'user': request.user.id})
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      print(serializer.errors)
    return Response(None)