from rest_framework.views import APIView, Response

from data.models import Category, Block, PrevLife, Scenario, Sexiness
from data.matrix import Matrix

from .filters import filter_blocks, filter_codes, filter_programs, filter_forecast, filter_health

class MatrixView(APIView):
  permission_classes = []
  
  def get(self, request, date1, date2 = ''):
    solo = date2 == ''
    day, month, year = map(int, date1.split('.'))
    matrix = Matrix(solo, day, month, year)
    if not solo:
      day2, month2, year2 = map(int, date2.split('.'))
      matrix2 = Matrix(False, day2, month2, year2)
      matrix += matrix2
      
    mapping = {
      'Прошлая жизнь': PrevLife,
      'Жизненный сценарий': Scenario,
      'Сексуальность': Sexiness
    }
    info = []
    for category in Category.objects.filter(solo=matrix.solo):
      block_types = category.block_types.all()
      data = []
      positions = category.positions.split(',') if category.positions else []
      if block_types.exists():
        for block_type in block_types:
          block = {
            'title': block_type.title if block_type.personal else 'Описание',
            'content': ''
          }
          if block_type.personal:
            block['content'] = filter_blocks(matrix, block_type)
          else:
            default = Block.objects.get(type=block_type)
            block['content'] = default.content
          data.append(block)
      else:
        if category.title in mapping.keys():
          Model = mapping[category.title]
          first = Model.objects.filter(code='0')
          if first.exists():
            data.append({
              'title': 'Описание',
              'content': first.first().content
            })
          data.append({
            'title': category.title,
            'content': filter_codes(matrix, Model, category.positions)
          })
        elif category.title == 'Программы':
          data, positions = filter_programs(matrix)
        elif category.title == 'Прогноз на год':
          data = filter_forecast(matrix)
        elif category.title == 'Здоровье':
          data = filter_health(matrix)
      info.append({
        'category': category.title,
        'blocks': data,
        'positions': positions
      })
        
    return Response({
      'info': info,
      **matrix.to_representation()
    })