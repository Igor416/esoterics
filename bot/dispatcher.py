import requests

from user.models import User
from esoterics.settings import BOT_TOKEN, CHANNEL_ID, CHAT_ID
from bot.util import Update, Reply, PhotoReply, ChatMember, Invoice
from bot.handlers import start, answer_pre_checkout_query, request_question, answer_question, show_balance, send_answer, unknown

ROOT = f'https://api.telegram.org/bot{BOT_TOKEN}'
raw_mapping = (
  (('/start',), start),
  (('/ask', 'Задать вопрос', 'Задать другой вопрос'), request_question),
  (('/balance', 'Проверить баланс'), show_balance)
)

mapping = dict()

for commands, handler in raw_mapping:
  for command in commands:
    mapping.update({command: handler})

class Dispatcher:
  @staticmethod
  def dispatch(update: Update):
    if hasattr(update, 'pre_checkout_query'):
      Dispatcher.answer_pre_checkout_query(update)
    elif hasattr(update.message, 'photo') and update.message.chat.id == int(CHAT_ID):
      Dispatcher.send_photo(update)
    else:
      handler = unknown
      user = User.objects.filter(id=update.message.chat.id)
      if user.exists():
        user = user.first()
        if update.message.text in mapping.keys():
          handler = mapping[update.message.text]
          user.last_action = update.message.text
        elif user.last_action in raw_mapping[1][0]:
          handler = answer_question
          user.last_action = '/request'
        user.save()
      else:
        handler = start
        
      messages = handler(update)
      Dispatcher.send_message(*messages)
  
  @staticmethod
  def answer_pre_checkout_query(update: Update):
    url = f'{ROOT}/answerPreCheckoutQuery'
    answer, reply = answer_pre_checkout_query(update)
    requests.post(url, data=answer.to_json())
    Dispatcher.send_message(reply)
  
  @staticmethod
  def send_message(*messages: Reply):
    url = f'{ROOT}/sendMessage'
    for message in messages:
      requests.post(url, data=message.to_json())
      
  @staticmethod
  def send_photo(update: Update):
    url = f'{ROOT}/sendPhoto'
    photo_reply = send_answer(update)
    requests.post(url, data=photo_reply.to_json())
  
  @staticmethod
  def upload_photo(photo_reply: PhotoReply, path: str):
    url = f'{ROOT}/sendPhoto'
    with open(path, 'rb') as photo:
      requests.post(url, data=photo_reply.to_json(), files={'photo': photo})
    
  @staticmethod
  def get_chat_member(user_id: int) -> ChatMember:
    url = f'{ROOT}/getChatMember'
    response = requests.post(url, data={
      'chat_id': CHANNEL_ID,
      'user_id': user_id
    })
    chat_member = ChatMember(**response.json()['result'])
    return chat_member
  
  @staticmethod
  def send_invoice(invoice: Invoice):
    url = f'{ROOT}/sendInvoice'
    requests.post(url, data=invoice.to_json())