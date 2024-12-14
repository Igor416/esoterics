from django.db import models
from django.utils.functional import cached_property
from uuid import uuid4

from data.names import ARCANES, SUITS, RANKS

class CardManager(models.Manager):
  def get_queryset(self) -> models.QuerySet:
    qs = super().get_queryset()
    ranks_order = models.Case(
      *[models.When(rank=rank, then=i) for i, rank in enumerate(Card.RANKS)],
      output_field=models.SmallIntegerField()
    )
    suits_order = models.Case(
      *[models.When(suit=suit, then=i) for i, suit in enumerate(Card.SUITS)],
      output_field=models.SmallIntegerField()
    )
    return qs.annotate(ranks=ranks_order, suits=suits_order).order_by('suits', 'ranks', 'arcane')

# Create your models here.
class Card(models.Model):
  ARCANES = ARCANES
  SUITS = { 'M': 'Старшие арканы', **SUITS }
  RANKS = { '0': 'Аркан', **RANKS }
  
  id = models.UUIDField(primary_key=True, default=uuid4)
  suit = models.CharField('Масть', max_length=1, default='M', choices=SUITS)
  rank = models.CharField('Стоимость', max_length=1, default='0', choices=RANKS)
  arcane = models.SmallIntegerField('Аркан', default=0)
  desc = models.TextField('Описание', blank=True)
  meaning1 = models.TextField('Прямое значение', blank=True)
  explanation1 = models.TextField('Прямое толкование', blank=True)
  meaning2 = models.TextField('Перевернутое значение', blank=True)
  explanation2 = models.TextField('Перевернутое толкование', blank=True)
  objects = CardManager()
  
  @cached_property
  def is_major(self):
    return self.rank == '0'
  
  @cached_property
  def name(self):
    if self.is_major:
      return f'{self.ARCANES[self.arcane]} ({self.arcane})'
    return f'{self.get_rank_display()} {self.get_suit_display()}'
  
  @cached_property
  def image(self):
    return f'static\cards\{self.suit.lower()}\{self.arcane if self.is_major else self.rank}.jpg'
  
  def __str__(self):
    return self.name
  
  class Meta:
    unique_together = ['suit', 'rank', 'arcane']
    verbose_name = 'Карта'
    verbose_name_plural = 'Карты'