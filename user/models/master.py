from django.db import models
from uuid import uuid4

from .user import User

class Master(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4)
  user = models.OneToOneField(User, verbose_name='аккаунт', on_delete=models.SET_NULL, null=True, blank=True)
  name = models.CharField('Имя', max_length=32)
  
  sunday_hours = models.CharField('Рабочие часы в вс', max_length=32, blank=True)
  monday_hours = models.CharField('Рабочие часы в пн', max_length=32, blank=True)
  tuesday_hours = models.CharField('Рабочие часы в вт', max_length=32, blank=True)
  wednesday_hours = models.CharField('Рабочие часы в ср', max_length=32, blank=True)
  thursday_hours = models.CharField('Рабочие часы в чт', max_length=32, blank=True)
  friday_hours = models.CharField('Рабочие часы в пт', max_length=32, blank=True)
  saturday_hours = models.CharField('Рабочие часы в сб', max_length=32, blank=True)
  
  class Meta:
    verbose_name = 'Мастер'
    verbose_name_plural = 'Мастера'
  
  def __str__(self):
    return self.name