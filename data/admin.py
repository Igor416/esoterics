from django.contrib import admin
from data.models import Category, BlockType, Block, PrevLife, Scenario, Program, Sexiness, Forecast

# Register your models here.
admin.site.register((Category, PrevLife, Scenario, Program, Sexiness, Forecast))

@admin.register(BlockType)
class BlockTypeAdmin(admin.ModelAdmin):
  list_filter = ['category', 'category__solo']
  
@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
  list_filter = ['type', 'type__category__solo']