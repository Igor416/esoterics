from data.models import CodeBlock
from data.matrix import Matrix

codes = [
  { 'positions': 'b,b1,b2', 'arcanes': [], 'content': [] },
  { 'positions': 'd,d1,d2', 'arcanes': [], 'content': [] },
  { 'positions': 'f,f1,f2', 'arcanes': [], 'content': [] },
  { 'positions': 'h,h1,h2', 'arcanes': [], 'content': [] },
  { 'positions': 'b,f,pm', 'arcanes': [], 'content': [] },
  { 'positions': 'd,h,pf', 'arcanes': [], 'content': [] },
  { 'positions': 's1,s2,s3', 'arcanes': [], 'content': [] },
  { 'positions': 's4,s5,s6', 'arcanes': [], 'content': [] },
  { 'positions': 'e2,xe,x', 'arcanes': [], 'content': [] },
  { 'positions': 'g2,xg,x', 'arcanes': [], 'content': [] },
  { 'positions': 't1,a,c', 'arcanes': [], 'content': [] },
  { 'positions': 't2,a1,c1', 'arcanes': [], 'content': [] },
  { 'positions': 't3,a2,c2', 'arcanes': [], 'content': [] },
  { 'positions': 't4,a3,c3', 'arcanes': [], 'content': [] },
  { 'positions': 't5,z,z', 'arcanes': [], 'content': [] },
  { 'positions': 't6,e2,g2', 'arcanes': [], 'content': [] },
  { 'positions': 't7,e,g', 'arcanes': [], 'content': [] },
  { 'positions': 't8,t9,t10', 'arcanes': [], 'content': [] },
]

def get_content(programs, code):
  for program in programs:
    arcanes = map(int, program.code.split('-')[1:-1])
    if all([arcane in code['arcanes'] for arcane in arcanes]):
      return [{
        'title': program.title,
        'arcanes': code['arcanes'],
        'text': program.content
      }]
  return []

def filter_programs(matrix: Matrix):
  for code in codes:
    for position in code.get('positions').split(','):
      code['arcanes'].append(matrix.combs[position])

  for code in codes:
    qs = CodeBlock.objects.filter(type__title='Программы')
    for arcane in sorted(code.get('arcanes')):
      qs = qs.filter(code__contains='-' + str(arcane) + '-')

    if qs.exists():
      code['content'] = get_content(qs, code)

  positions = list()
  used = list()
  data = []
  for code in codes:
    if code['content']:
      positions.extend(code['positions'].split(','))
      title = code['content'][0].pop('title')
      if title not in used:
        data.append({
          'title': title,
          'content': code['content']
        })
        used.append(title)

  return (data, positions)