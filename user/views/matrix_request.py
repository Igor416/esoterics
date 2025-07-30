from rest_framework.views import APIView, Response

from user.serializers import MatrixRequestSerializer
from user.models import MatrixRequest

class MatrixRequestsView(APIView):
  def get(self, request, id = 'all'):
    queryset = MatrixRequest.objects.filter(user=request.user)
    if id != 'all':
      queryset = MatrixRequest.objects.filter(id=id)
      if queryset.exists():
        serializer = MatrixRequestSerializer(queryset.first())
      return Response(None)
    else:
      serializer = MatrixRequestSerializer(queryset, many=True)
    return Response(serializer.data)
  
  def post(self, request):
    id = request.data.pop('id', '')
    if id:
      queryset = MatrixRequest.objects.filter(id=id)
    else:
      queryset = MatrixRequest.objects.filter(user=request.user, **request.data)
      
    if queryset.exists() and queryset.first().user == request.user:
      return Response(None)
      
    serializer = MatrixRequestSerializer(data={**request.data, 'user': request.user.id})
      
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      print(serializer.errors)
      
    return Response(None)
  
  def delete(self, request, id = 'all'):
    if id == 'all':
      MatrixRequest.objects.filter(user=request.user).delete()
      return Response([])
    
    queryset = MatrixRequest.objects.filter(id=id)
    queryset.delete()
    queryset =  MatrixRequest.objects.filter(user=request.user)
    serializer = MatrixRequestSerializer(queryset, many=True)
    return Response(serializer.data)