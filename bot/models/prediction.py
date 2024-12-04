from django.db import models
from uuid import uuid4
from random import choice

from data.models import Card

class PredictionManager(models.Manager):
  def get_queryset(self) -> models.QuerySet:
    qs = super().get_queryset()
    card_ranks_order = models.Case(
      *[models.When(card__rank=rank, then=i) for i, rank in enumerate(Card.RANKS)],
      output_field=models.SmallIntegerField()
    )
    card_suits_order = models.Case(
      *[models.When(card__suit=suit, then=i) for i, suit in enumerate(Card.SUITS)],
      output_field=models.SmallIntegerField()
    )
    return qs.annotate(
      card_ranks=card_ranks_order,
      card_suits=card_suits_order
    ).order_by('card_suits', 'card_ranks', 'card__arcane', 'order')

# Create your models here.
class Prediction(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4)
  card = models.ForeignKey(Card, on_delete=models.CASCADE, verbose_name='Карта', related_name='predictions')
  order = models.SmallIntegerField('Порядок', default=1)
  used = models.BooleanField('Использована', default=False)
  content = models.TextField('Контент', blank=True)
  objects = PredictionManager()
  
  @staticmethod
  def choose_prediction(qs: models.QuerySet) -> 'Prediction':
    order = choice(qs.filter(used=False).values_list('order', flat=True))
    prediction = qs.filter(order=order)
    prediction.update(used=True)
    if not qs.filter(used=False).exists():
      qs.exclude(order=order).update(used=False)
    return prediction.first()
  
  def __str__(self):
    return f'{self.card}, #{self.order}'
  
  def print(self):
    start = 'Младший аркан дня 💫'
    if self.card.is_major:
      start = 'Позитивная энергия дня ☀️' if self.order < 11 else 'Негативная энергия дня ☁️'
    return f'<b>{start} - {self.card}</b>' + '\n' + self.content
  
  class Meta:
    verbose_name = 'Предсказание'
    verbose_name_plural = 'Предсказания'