from rest_framework.views import APIView, Response

from user.serializers import MatrixRequestSerializer
from user.models import MatrixRequest

class MatrixRequestsView(APIView):
  def format_queryset(self, qs):
    paired = qs.exclude(paired=None)
    single = qs.filter(paired=None).exclude(id__in=paired.values_list('paired__id', flat=True))
    return (single | paired).order_by('created')
  
  def get(self, request, id = ''):
    queryset = self.format_queryset(MatrixRequest.objects.filter(user=request.user))
    if id:
      queryset = MatrixRequest.objects.filter(id=id)
      paired = queryset.first().paired
      if not paired and hasattr(queryset.first(), 'pair'):
        paired = queryset.first().pair
      if paired:
        queryset |= MatrixRequest.objects.filter(id=paired.id)
    else:
      queryset = self.format_queryset(MatrixRequest.objects.filter(user=request.user))
    serializer = MatrixRequestSerializer(queryset, many=True)
    return Response(serializer.data)
  
  def post(self, request):
    id = request.data.pop('id', '')
    if id:
      queryset = MatrixRequest.objects.filter(id=id)
    else:
      queryset = MatrixRequest.objects.none()
      
    if queryset.exists() and queryset.first().user == request.user:
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