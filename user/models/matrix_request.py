from django.db import models
from .user import User
from uuid import uuid4

class MatrixRequest(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4)
  name = models.CharField('Имя', max_length=32)
  gender = models.CharField('Гендер', choices={'m': 'парень', 'f': 'девушка'}, max_length=1)
  date = models.CharField('Дата рождения', max_length=10)
  paired = models.OneToOneField('self', on_delete=models.CASCADE, null=True, blank=True)
  created = models.DateTimeField('Создан', auto_now_add=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
  
  class Meta:
    verbose_name = 'Запрос по матрице'
    verbose_name_plural = 'Запросы по матрице'
    ordering = ['created']
  
  def __str__(self):
    return f'{self.name} {"♂" if self.gender == "m" else "♀"} ${self.date}'