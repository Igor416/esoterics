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
  for_codes = models.BooleanField('Для блоков с кодом', default=False)
  order = models.SmallIntegerField('Порядок', default=1)
  
  def __str__(self):
    s = f'{self.title if self.title else "Общее"}, категория: {self.category}'
    if self.personal:
      if len(self.positions) != 0:
        s += ', позиции: ' + self.positions
    else:
      s += ', общий'
    return s
  
  class Meta:
    ordering = ['category__solo', 'category__order', 'order']
    unique_together = ['order', 'category']
    verbose_name = 'Тип Блоков'
    verbose_name_plural = 'Типы Блоков'