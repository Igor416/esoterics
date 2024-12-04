from data.models import Block
from data.matrix import Matrix

mapping = ['0', '1-2.5', '2.5-3.5', '3.5-4', '5', '6-7.5', '7.5-8.5', '8-9.5']

def get_block(matrix: Matrix, letter: int, number: int):
  content = ''
  age = '-'.join(map(lambda x: str((float(x) if '.' in x else int(x)) + letter * 10).replace('.', ','), mapping[number].split('-')))
  pos = matrix.nums['abcdefgh'[letter] + str(number if number > 0 else '')]
  opp = matrix.nums['abcdefgh'[letter + 4 if letter < 4 else letter - 4] + str(number if number > 0 else '')]
  sum = Matrix.Positions.round(pos + opp)
    
  arcanes = [pos]
  if opp != pos:
    arcanes.append(opp)
  if sum not in arcanes:
    arcanes.append(sum)
    
  queryset = Block.objects.filter(type__title='Прогноз на год')
  for arcane in arcanes:
    forecast = queryset.get(arcane=arcane)
    content += f'({arcane}) {forecast.content}' + '\n\n'
  
  return {
    'title': age,
    'content': content
  }

def filter_forecast(matrix: Matrix):
  resp = []
  for i in range(8):
    for j in range(8):
      if i == 0 and j == 0:
        continue
      resp.append(get_block(matrix, i, j))
  resp.append({
    'title': '80',
    'content': get_block(matrix, i, j)['content']
  })
  
  return resp