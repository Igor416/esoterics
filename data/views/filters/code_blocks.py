from data.models import BlockType
from data.matrix import Matrix

def filter_code_blocks(matrix: Matrix, block_type: BlockType):
  arcanes = list()
  for position in block_type.positions.split(','):
    arcanes.append(str(matrix.combs[position]))
  
  qs = block_type.code_blocks.filter(code='-'.join(arcanes))
  
  if qs.exists():
    return [{
      'title': block_type.title,
      'content': [{
        'arcanes': map(int, qs.first().code.split('-')),
        'text': qs.first().content
      }]
    }]
  else:
    print(f'Не существует блока {block_type.title} с кодом ({"-".join(map(str, arcanes))})')
  
  return ''