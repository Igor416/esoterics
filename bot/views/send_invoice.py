from rest_framework.views import APIView, Response

from bot.models import Transaction
from bot.util import LabeledPrice, Invoice
from bot.dispatcher import Dispatcher

class SendInvoiceView(APIView):
  def post(self, request):
    amount = request.data['amount']
    transaction = Transaction.objects.create(user=request.user, price=amount * 50)
    invoice = Invoice(
      chat_id=request.user.id,
      title=f'Вопросы для расклада: {amount}',
      description=f'Вам начислятся вопросы ({amount}) на баланс аккаунта и вы сможете задать их, нажав кнопку в следующем сообщении после оплаты',
      payload=str(transaction.id),
      provider_token='',
      currency='XTR',
      prices=[LabeledPrice(label=f'{transaction.price}⭐️', amount=transaction.price)]
    )
    Dispatcher.send_invoice(invoice)
    return Response(True)