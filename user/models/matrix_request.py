from django.db import models
from .user import User
from uuid import uuid4

class MatrixRequest(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4)
  name = models.CharField('Имя', max_length=32)
  date = models.CharField('Дата рождения', max_length=10)
  gender = models.CharField('Гендер', choices={'m': 'парень', 'f': 'девушка', 'c': 'совместимость'}, max_length=1)
  name2 = models.CharField('Имя 2', max_length=32, blank=True)
  date2 = models.CharField('Дата рождения 2', max_length=10, blank=True)
  created = models.DateTimeField('Создан', auto_now_add=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='requests')
  
  class Meta:
    verbose_name = 'Запрос по матрице'
    verbose_name_plural = 'Запросы по матрице'
    ordering = ['created']
  
  def __str__(self):
    return f'{self.name} {self.date}{f" + {self.name2} {self.date2}" if self.name2 else ""}'