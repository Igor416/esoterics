from django.db import models
from uuid import uuid4

from .block_type import BlockType

# Create your models here.
class Block(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4)
  type = models.ForeignKey(BlockType, related_name='blocks', on_delete=models.SET_NULL, null=True, default=None, verbose_name='Тип блока')
  content = models.TextField('Контент', blank=True)
  arcane = models.SmallIntegerField('Аркан', default=0)
  
  def __str__(self):
    return f'{self.type}, аркан: {self.arcane}'
  
  class Meta:
    ordering = ['type__category__solo', 'type__category__order', 'type__order', 'arcane']
    verbose_name = 'Блок'
    verbose_name_plural = 'Блоки'