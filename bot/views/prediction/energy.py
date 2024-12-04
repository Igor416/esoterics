from datetime import date, timedelta

from bot.models import Prediction

from .main import PredictionView

class EnergyView(PredictionView):
  positive = True
  
  def get_opposite_date(d1: date):
    year = d1.year
    is_leap = (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
    total_days = 366 if is_leap else 365
    
    start_of_year = date(year, 1, 1)
    days_passed = (d1 - start_of_year).days + 1
    
    days_remaining = total_days - days_passed
    d2 = start_of_year + timedelta(days=days_remaining)
    
    return d2
  
  def get(self, request):
    today = date.today()
    if not self.positive:
      today = self.get_opposite_date(today)
    date_hash = self.get_hash(today)
    arcane = date_hash % 22
    qs = Prediction.objects.filter(card__arcane=arcane, **({'order__lt': 11} if self.positive else {'order__gt': 10}))
    return super().get(request, qs)