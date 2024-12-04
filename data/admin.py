from django.contrib import admin
from data.models import Category, BlockType, Block, CodeBlock, Card

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_filter = ['solo']

@admin.register(BlockType)
class BlockTypeAdmin(admin.ModelAdmin):
  list_filter = ['category', 'category__solo']
  
class BlockTypeFilter(admin.SimpleListFilter):
  title = 'Тип Блока'
  parameter_name = 'type__id__exact'

  def lookups(self, request, model_admin):
    queryset = BlockType.objects.filter(for_codes=model_admin.title == 'Блоки с Кодом')
    return queryset.values_list('id', 'title')

  def queryset(self, request, queryset):
    if self.value():
      return queryset.filter(**{self.parameter_name: self.value()})
    return queryset

@admin.register(CodeBlock)
class CodeBlockAdmin(admin.ModelAdmin):
  title = 'Блоки с Кодом'
  list_filter = [BlockTypeFilter, 'type__category__solo']
  
  def lookup_allowed(self, key, value=None):
    return True
  
@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
  title = 'Блоки'
  list_filter = [BlockTypeFilter, 'type__category__solo']
  
  def lookup_allowed(self, key, value=None):
    return True
  
@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
  list_filter = ['suit', 'rank', 'arcane']
