from data.models import BlockType
from data.matrix import Matrix

def filter_blocks(matrix: Matrix, block_type: BlockType):
  resp = []
  arcanes = set()
  if block_type.positions:
    for position in block_type.positions.split(','):
      arcanes.add(matrix.combs[position])
  
  for arcane in sorted(list(arcanes)):
    block = block_type.blocks.filter(arcane=arcane)
    if block.exists():
      resp.append(f'({arcane}) {block.first().content}')
    else:
      print(f'Не существует блока с типом: {block_type} и арканом ({arcane})')
  
  return '\n'.join(resp)