from rest_framework.views import APIView, Response

from bot.dispatcher import Dispatcher

class CheckSubscriptionView(APIView):
  def post(self, request):
    chat_member = Dispatcher.get_chat_member(request.user.id)
    return Response(chat_member.status != 'left')