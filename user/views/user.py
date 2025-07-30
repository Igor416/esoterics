from rest_framework.views import APIView, Response, Request
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenRefreshSerializer

from user.serializers import UserSerializer
from user.models import User

class UserView(APIView):
  permission_classes = []
  
  def get(self, request: Request):
    return Response(UserSerializer(request.user).data)
  
  def post(self, request: Request):
    query = User.objects.filter(id=request.data.get('id'))
    if query.exists():
      user = query.first()
      serializer = UserSerializer(user, data=request.data)
    else:
      serializer = UserSerializer(data=request.data)
      
    if serializer.is_valid():
      user = serializer.save()
      refresh = RefreshToken.for_user(user)
      return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
      })
      
    return Response(None)
  
class RefreshView(APIView):
  authentication_classes = []
  permission_classes = []
  
  def post(self, request):
    serializer = TokenRefreshSerializer(data=request.data)
    if serializer.is_valid():
      return Response(serializer.data)
    return Response('')