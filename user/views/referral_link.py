from rest_framework.views import APIView, Response
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from user.serializers import UserSerializer
from user.models import User, ReferralLink

class ReferralLinkView(APIView):
  def post(self, request):
    link = ReferralLink.objects.create(user=request.user)
    user = link.user
    serializer = UserSerializer(user)
    return Response(serializer.data)