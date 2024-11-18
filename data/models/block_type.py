from django.db import models
from uuid import uuid4

from .category import Category

# Create your models here.
class BlockType(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4)
  category = models.ForeignKey(Category, related_name='block_types', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Категория')
  title = models.CharField('Название', max_length=64, blank=True)
  positions = models.CharField('Позиции', max_length=35, blank=True)
  personal = models.BooleanField('Личный', default=True)
  order = models.SmallIntegerField('Порядок', default=1)
  
  def __str__(self):
    return f'{self.title if self.title else "Общее"}, категория: {self.category}, {"позиции: " + self.positions if self.personal else "общий"}'
  
  class Meta:
    ordering = ['category__solo', 'category__order', 'order']
    unique_together = ['order', 'category']
    verbose_name = 'Тип Блоков'
    verbose_name_plural = 'Типы Блоков'