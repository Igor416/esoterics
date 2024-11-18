from django.db import models
from uuid import uuid4

# Create your models here.
class Forecast(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4)
  arcane = models.SmallIntegerField('Аркан', default=0)
  content = models.TextField('Контент', blank=True)
  
  def __str__(self):
    return f'{self.arcane}'
  
  class Meta:
    ordering = ['arcane']
    verbose_name = 'Прогноз'
    verbose_name_plural = 'Прогнозы'