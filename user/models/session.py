from django.db import models
from .user import User
from .master import Master
from uuid import uuid4

class Session(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4)
  customer = models.ForeignKey(User, verbose_name='покупатель', on_delete=models.SET_NULL, null=True)
  master = models.ForeignKey(Master, verbose_name='мастер', on_delete=models.SET_NULL, null=True)
  plan = models.CharField('План', choices={
    'A': 'Материальное',
    'B': 'Самочувствие',
    'C': 'Отношения'
  }, max_length=1)
  online = models.BooleanField('Онлайн')
  date = models.DateTimeField('Дата и время')
  status = models.CharField('Статус', choices={
    'O': 'Заказана',
    'A': 'Одобрена',
    'S': 'Начата',
    'F': 'Окончена'
  }, max_length=1)
  paid = models.BooleanField('Оплачена')
  
  @property
  def price(self):
    pricelist = {'A': 200, 'B': 250, 'C': 200}
    return pricelist[self.plan]
  
  class Meta:
    verbose_name = 'Сессия'
    verbose_name_plural = 'Сессии'
  
  def __str__(self):
    return f'{self.master}: {self.date.strftime("%d.%m - %H")}:00, план {self.plan}, статус - {self.get_status_display()}'