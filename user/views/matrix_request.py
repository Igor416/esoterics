from rest_framework.views import APIView, Response

from user.serializers import MatrixRequestSerializer
from user.models import MatrixRequest

class MatrixRequestsView(APIView):
  def format_queryset(self, qs):
    paired = qs.exclude(paired=None)
    single = qs.filter(paired=None).exclude(id__in=paired.values_list('paired__id', flat=True))
    return (single | paired).order_by('created')
  
  def get(self, request):
    queryset = self.format_queryset(MatrixRequest.objects.filter(user=request.user))
    serializer = MatrixRequestSerializer(queryset, many=True)
    return Response(serializer.data)
  
  def post(self, request):
    queryset = MatrixRequest.objects.filter(id=request.data.get('id'))
    
    if queryset.exists():
      return Response(None)
      
    serializer = MatrixRequestSerializer(data={**request.data, 'user': request.user.id})
      
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      print(serializer.errors)
      
    return Response(None)
  
  def delete(self, request):
    id = request.data.get('id')
    if id == 'all':
      MatrixRequest.objects.filter(user=request.user).delete()
      return Response([])
    
    queryset = MatrixRequest.objects.filter(id=id)
    if not queryset.exists():
      return Response(None)
    
    queryset.delete()
    queryset =  self.format_queryset(MatrixRequest.objects.filter(user=request.user))
    serializer = MatrixRequestSerializer(queryset, many=True)
    return Response(serializer.data)