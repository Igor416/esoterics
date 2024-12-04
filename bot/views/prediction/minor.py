from datetime import date

from data.names import SUITS, RANKS
from bot.models import Prediction

from .main import PredictionView

class MinorView(PredictionView):
  permission_classes = []
  
  def get(self, request):
    today = date.today()
    hash = self.get_hash(today)
    pivot = hash % 56
    suit = list(SUITS.keys())[pivot // 14]
    rank = list(RANKS.keys())[pivot % 14]
    qs = Prediction.objects.filter(card__suit=suit, card__rank=rank)
    return super().get(request, qs)