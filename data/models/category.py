from django.db import models
from uuid import uuid4

# Create your models here.
class Category(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4)
  title = models.CharField('Название', max_length=32)
  positions = models.CharField('Позиции', max_length=48, blank=True)
  order = models.SmallIntegerField('Порядок', default=1)
  solo = models.BooleanField('Одиночная матрица', default=True)
  
  def __str__(self):
    return f'{self.title} - {"Одиночная" if self.solo else "Совместимость"}'
  
  class Meta:
    ordering = ['solo', 'order']
    unique_together = ['solo', 'order']
    verbose_name = 'Категория'
    verbose_name_plural = 'Категории'