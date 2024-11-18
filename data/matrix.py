class Matrix:
  primaries = ('a', 'c', 'e', 'g')
  secondaries = ('b', 'd', 'f', 'h')
  
  class Positions:
    def __init__(self, copy = None):
      self.fields = []
      if copy:
        for field in copy.fields:
          self[field] = copy[field]
        
    def __getitem__(self, name) -> int:
      return getattr(self, name)
    
    def __setitem__(self, name, value):
      setattr(self, name, value)
    
    def __setattr__(self, name, value):
      if name != 'fields':
        self.fields.append(name)
        if isinstance(value, tuple):
          values = [self[val] for val in value]
          value = sum(values)
        value = self.round(value)
      super().__setattr__(name, value)
      
    @staticmethod
    def round(value):
      while value > 22:
        s = 0
        for el in str(value):
          s += int(el)
        value = s
      return value
        
  def __init__(self, solo, day, month, year):
    self.solo = solo
    self.dates = self.Positions()
    self.dates.day, self.dates.month, self.dates.year = day, month, year
    
    self.positions = []
    fillers = [self.fill_combs, self.fill_miscellaneous]
    if self.solo:
      fillers.extend([self.fill_nums, self.fill_health])
    for filler in fillers:
      self.positions.append(filler())
  
  def __add__(self, other):
    for field in self.primaries + self.secondaries + ('z',):
      self.combs[field] += other.combs[field]
    self.combs = self.calc_combs()
    self.combs = self.fill_miscellaneous()
    return self
  
  def fill_combs(self):
    self.combs = self.Positions()
    #primary
    self.combs.a = self.dates.day
    self.combs.c = self.dates.month
    self.combs.e = self.dates.year
    self.combs.g = ('a', 'c', 'e')
    #secondary
    self.combs.b = ('a', 'c')
    self.combs.d = ('c', 'e')
    self.combs.f = ('e', 'g')
    self.combs.h = ('g', 'a')
    
    if self.solo:
      self.nums = self.Positions(self.combs)
    #comfort
    self.combs.z = self.primaries
    if self.solo:
      self.combs.z1 = self.secondaries
      self.combs.z2 = ('z', 'z1')
    
    return self.calc_combs()
  
  def calc_combs(self):
    #primary parts
    for primary in self.primaries:
      self.combs[primary + '2'] = (primary, 'z')
      self.combs[primary + '1'] = (primary, primary + '2')
    if self.solo:
      self.combs.a3 = ('a2', 'z')
      self.combs.c3 = ('c2', 'z')
    #secondary parts
    if self.solo:
      for secondary in self.secondaries:
        self.combs[secondary + '2'] = (secondary, 'z1')
        self.combs[secondary + '1'] = (secondary, secondary + '2')
    #heart and money
    self.combs.x = ('e2', 'g2')
    self.combs.xe = ('x', 'e2')
    self.combs.xg = ('x', 'g2')
    
    return self.combs
    
  def fill_nums(self):
    pairs = (('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'f'), ('f', 'g'), ('g', 'h'), ('h', 'a'))
    
    for x, y in pairs:
      self.nums[x + '4'] = (x, y)
      
      self.nums[x + '2'] = (x, x + '4')
      self.nums[x + '6'] = (x + '4', y)
      
      self.nums[x + '1'] = (x, x + '2')
      self.nums[x + '3'] = (x + '2', x + '4')
      self.nums[x + '5'] = (x + '4', x + '6')
      self.nums[x + '7'] = (x + '6', y)
    
    return self.nums
      
  def fill_health(self):
    self.combs.t1 = ('a', 'c')
    self.combs.t2 = ('a1', 'c1')
    self.combs.t3 = ('a2', 'c2')
    self.combs.t4 = ('a3', 'c3')
    self.combs.t5 = ('z', 'z')
    self.combs.t6 = ('e2', 'g2')
    self.combs.t7 = ('e', 'g')
    self.combs.t8 = ('a', 'a1', 'a2', 'a3', 'z', 'e2', 'e')
    self.combs.t9 = ('c', 'c1', 'c2', 'c3', 'z', 'g2', 'g')
    self.combs.t10 = ('t1', 't2', 't3', 't4', 't5', 't6', 't7')
    
    return self.combs
  
  def fill_miscellaneous(self):
    if self.solo:
      self.combs.pm = ('b', 'f')
      self.combs.pf = ('d', 'h')
    
    self.combs.s1, self.combs.s2 = self.combs.c + self.combs.g, self.combs.a + self.combs.e
    self.combs.s3 = ('s1', 's2')
    self.combs.s4, self.combs.s5 = self.combs.b + self.combs.f, self.combs.d + self.combs.h
    self.combs.s6 = ('s4', 's5')
    
    self.combs.w = ('s3', 's6')
    return self.combs
  
  def to_representation(self):
    r = {'combinations': {field: self.combs[field] for field in self.combs.fields}}
    if self.solo:
      r['numbers'] = {field: self.nums[field] for field in self.nums.fields}
    return r