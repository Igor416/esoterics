from django.db import models

class User(models.Model):
  id = models.BigIntegerField('ID', primary_key=True)
  first_name = models.CharField('Имя', max_length=32, blank=True)
  last_name = models.CharField('Фамилия', max_length=32, blank=True)
  username = models.CharField('Имя пользователя @', max_length=32, unique=True)
  language_code = models.CharField('Язык', default='ru', max_length=2)
  
  questions = models.SmallIntegerField('Баланс вопросов', default=0)
  last_action = models.TextField('Последнее действие', default='/start')
  
  is_active = True
  is_authenticated = False
  
  class Meta:
    verbose_name = 'Пользователь'
    verbose_name_plural = 'Пользователи'
  
  def __str__(self):
    return self.first_name + ' ' + self.last_name