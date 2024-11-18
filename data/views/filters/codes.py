from django.db.models import Model
from data.matrix import Matrix

def filter_codes(matrix: Matrix, Model: Model, positions: str):
  arcanes = list()
  for position in positions.split(','):
    arcanes.append(str(matrix.combs[position]))
  
  qs = Model.objects.filter(code='-'.join(arcanes))
  
  if qs.exists():
    return qs.first().content
  else:
    print(f'Не существует модели {Model} с арканами ({'-'.join(map(str, arcanes))})')
  
  return ''