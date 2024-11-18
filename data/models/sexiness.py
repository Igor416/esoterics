from django.db import models
from uuid import uuid4

# Create your models here.
class Sexiness(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4)
  code = models.CharField('Код', max_length=10)
  content = models.TextField('Контент', blank=True)
  
  def __str__(self):
    return f'{self.code}'
  
  class Meta:
    ordering = ['code']
    verbose_name = 'Сексуальность'
    verbose_name_plural = 'Сексуальности'