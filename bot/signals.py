from django.db.models.signals import post_save
from django.dispatch import receiver
from esoterics.settings import BOT_TOKEN, CHAT_ID
from user.models import Session
import requests

@receiver(post_save, sender=Session, dispatch_uid='on_session_ordered')
def on_session_saved(sender, **kwargs):
  session = kwargs.pop('instance')
  url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
  messages = get_messages(session)
  for message in messages:
    requests.post(url, data=message)
  
def get_messages(session: Session):
  mapping = {
    'O': handle_order,
    'A': handle_approve,
    'S': handle_start,
    'F': handle_finish
  }
  return mapping[session.status](session)
  
def handle_order(session: Session):
  data = [
    '',
    f'клиент: @{session.customer.username}',
    f'тип расклада: {session.get_plan_display()}',
    f'режим: {"онлайн" if session.online else "оффлайн"}',
    f'дата и время: {session.date.strftime("%d.%m - %H")}:00'
  ]
  return [
    {
      'chat_id': CHAT_ID, 
      'text': 'Добавлена одна сессия'
    },
    {
      'chat_id': session.master.user.id,
      'text': f'Пользователь заказал расклад, данные:' + '\n'.join(data),
    },
    {
      'chat_id': session.customer.id,
      'text': 'Ваш заказ получен, скоро с вами свяжется специалист для уточнения деталей (место встречи / платформа видеосвязи)',
    }
  ]
  
def handle_approve(session: Session):
  return []
  
def handle_start(session: Session):
  return []
  
def handle_finish(session: Session):
  return []