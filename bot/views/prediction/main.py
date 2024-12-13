from rest_framework.views import APIView, Response
from datetime import date
import hashlib

from esoterics.settings import CHANNEL_ID
from bot.util import MediaGroup, InputMediaPhoto, MessageEntity
from bot.models import Prediction
from bot.dispatcher import Dispatcher

class PredictionView(APIView):
  permission_classes = []
  
  def get_hash(self, date: date) -> int:
    date_str = date.strftime('%Y-%m-%d')
    hash_value = hashlib.sha256(date_str.encode()).hexdigest()
    hash_int = int(hash_value, 16)
    return hash_int
  
  def get(self, request, qs):
    prediction = Prediction.choose_prediction(qs)
    caption = prediction.print()
    media_group = MediaGroup(chat_id=CHANNEL_ID, media=[
      InputMediaPhoto(type='photo', media=prediction.card.image, caption=caption, parse_mode='HTML', caption_entities=[
        MessageEntity(type='bold', offset=0, length=caption.index('</b>') + 5)
      ])
    ])
    Dispatcher.send_media_group(media_group)
    return Response(None)