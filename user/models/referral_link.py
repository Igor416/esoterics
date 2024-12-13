from django.db import models
from uuid import uuid4

class ReferralLink(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4)
  user = models.OneToOneField('User', verbose_name='Пользователь', on_delete=models.CASCADE, unique=True, related_name='referral_link')
  created = models.DateTimeField('Создана', auto_now_add=True)
  
  class Meta:
    verbose_name = 'Реферальная ссылка'
    verbose_name_plural = 'Реферальные ссылки'
    ordering = ['-created']
  
  def __str__(self):
    return f'{self.user}'