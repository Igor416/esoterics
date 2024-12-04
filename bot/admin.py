from django.contrib import admin
from bot.models import Prediction, Transaction

# Register your models here.
@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
  list_filter = ['card__suit', 'card__rank', 'card__arcane', 'used']
  
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
  list_filter = ['finalised']