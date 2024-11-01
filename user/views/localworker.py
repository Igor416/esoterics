from rest_framework.views import APIView, Response

from user import models

class LocalWorkerView(APIView):
  def get(self, request):
    user = models.User.objects.first()
    subscrition = models.Subscription.objects.first()
    print(dir(user))
    print(dir(subscrition))
    return Response(None)
