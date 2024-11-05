from django.db.models.signals import post_save
from django.dispatch import receiver
from esoterics.settings import BOT_TOKEN, CHAT_ID
from user.models import Session
import requests

@receiver(post_save, sender=Session, dispatch_uid='on_session_ordered')
def on_session_ordered(sender, **kwargs):
  url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
  data = {
    'chat_id': CHAT_ID, 
    'text': 'Добавлена одна сессия'
  }
  requests.post(url, data=data)