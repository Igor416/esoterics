from rest_framework.views import APIView, Response

from data.models import Category, Block
from data.matrix import Matrix

from .filters import filter_blocks, filter_code_blocks, filter_programs, filter_forecast, filter_health

class MatrixView(APIView):
  permission_classes = []
  
  def get(self, request, date1: str, date2 = ''):
    solo = date2 == ''
    day, month, year = map(int, date1.split('.'))
    matrix = Matrix(solo, day, month, year)
    if not solo:
      day2, month2, year2 = map(int, date2.split('.'))
      matrix2 = Matrix(False, day2, month2, year2)
      matrix += matrix2
      
    info = []
    mapping = {
      'Программы': filter_programs,
      'Прогноз на год': filter_forecast,
      'Здоровье': filter_health
    }
    for category in Category.objects.filter(solo=matrix.solo):
      positions = category.positions.split(',') if category.positions else []
      data = []
      block_types = category.block_types.all()
      if category.title in mapping:
        data, positions = mapping[category.title](matrix)
      elif block_types.filter(for_codes=True).exists():
        data = filter_code_blocks(matrix, block_types.first())
      else:
        for block_type in block_types:
          block = {
            'title': block_type.title if block_type.personal else 'Описание'
          }
          if block_type.personal:
            block['content'] = filter_blocks(matrix, block_type)
          else:
            default = Block.objects.get(type=block_type)
            block['content'] = [{
              'arcanes': [],
              'text': default.content
            }]
          data.append(block)
        
      info.append({
        'category': category.title,
        'blocks': data,
        'positions': positions
      })
        
    return Response({
      'info': info,
      **matrix.to_representation()
    })