from data.models import Block
from data.matrix import Matrix

def filter_health(matrix: Matrix):
  data = [
    { 'positions': 't1,a,c', 'content': [] },
    { 'positions': 't2,a1,c1', 'content': [] },
    { 'positions': 't3,a2,c2', 'content': [] },
    { 'positions': 't4,a3,c3', 'content': [] },
    { 'positions': 't5,z,z', 'content': [] },
    { 'positions': 't6,e2,g2', 'content': [] },
    { 'positions': 't7,e,g', 'content': [] },
    { 'positions': 't8,t9,t10', 'content': [] },
  ]
  blocks = Block.objects.filter(type__title='Здоровье')
  for object in data:
    arcanes = set()
    for position in object.get('positions').split(','):
      arcanes.add(matrix.combs[position])
    for arcane in sorted(list(arcanes)):
      object['content'].append({
        'arcanes': [arcane],
        'text': blocks.get(arcane=arcane).content
      })
    
  resp = []
  for object in data:
    resp.append({
      'title': '',
      'content': object['content']
    })
    
  return (resp, blocks.first().type.positions)