from django.db import models

from .referral_link import ReferralLink

class User(models.Model):
  id = models.BigIntegerField('ID', primary_key=True)
  first_name = models.CharField('Имя', max_length=32, blank=True)
  last_name = models.CharField('Фамилия', max_length=32, blank=True)
  username = models.CharField('Имя пользователя @', max_length=32, blank=True)
  language_code = models.CharField('Язык', default='ru', max_length=2)
  
  fields = ('id', 'first_name', 'last_name', 'username', 'language_code')
  
  questions = models.SmallIntegerField('Баланс вопросов', default=0)
  last_action = models.TextField('Последнее действие', default='/start')
  
  joined_by = models.ForeignKey(ReferralLink, on_delete=models.SET_NULL, null=True, default=None, blank=True, verbose_name='Присоеденился по ссылке', related_name='referrals')
  
  is_active = True
  is_authenticated = False
  
  class Meta:
    verbose_name = 'Пользователь'
    verbose_name_plural = 'Пользователи'
  
  def __str__(self):
    return self.first_name + ' ' + self.last_name