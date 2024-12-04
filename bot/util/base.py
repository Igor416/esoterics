class Base:
  def __init__(self, **kwargs):
    self.fields = []
    for key, value in kwargs.items():
      setattr(self, key, value)
      if hasattr(value, 'fields'):
        continue
      self.fields.append(key)
      
  def to_json(self):
    r = dict()
    for key in self.fields:
      r.update({key: getattr(self, key)})
    return r