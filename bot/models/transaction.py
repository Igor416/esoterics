from django.db import models
from django.utils.functional import cached_property
from uuid import uuid4

from user.models import User

# Create your models here.
class Transaction(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4)
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Пользователь', related_name='transactions')
  price = models.SmallIntegerField('Стоимость (в звездах)', default=100)
  finalised = models.BooleanField('Окончена', default=False)
  
  @cached_property
  def amount(self):
    return self.price / 50
  
  def __str__(self):
    return f'{self.user}, стоимость: {self.price}'
  
  class Meta:
    verbose_name = 'Транзакция'
    verbose_name_plural = 'Транзакции'