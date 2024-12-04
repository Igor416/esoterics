from django.db import models
from uuid import uuid4

from .block_type import BlockType

# Create your models here.
class CodeBlock(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4)
  type = models.ForeignKey(BlockType, related_name='code_blocks', on_delete=models.SET_NULL, null=True, default=None, verbose_name='Тип блока')
  title = models.CharField('Название', max_length=32, blank=True)
  content = models.TextField('Контент', blank=True)
  code = models.CharField('Код', max_length=10)
  
  def __str__(self):
    return f'{self.title} {self.code}'
  
  class Meta:
    ordering = ['type__category__order', 'code']
    verbose_name = 'Блок с кодом'
    verbose_name_plural = 'Блоки с кодом'