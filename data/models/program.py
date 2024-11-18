from django.db import models
from uuid import uuid4

# Create your models here.
class Program(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4)
  title = models.CharField('Название', max_length=32)
  code = models.CharField('Код', max_length=10)
  content = models.TextField('Контент', blank=True)
  
  def __str__(self):
    return f'{self.title}'
  
  class Meta:
    ordering = ['code']
    verbose_name = 'Программа'
    verbose_name_plural = 'Программы'