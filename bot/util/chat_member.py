from .base import Base

class User(Base):
  id: int
  first_name: str
  last_name: str
  username: str
  language_code: str

class ChatMember(Base):
  status: str
  user: User
  
  def __init__(self, **kwargs):
    self.user = User(**kwargs.pop('user'))
    super().__init__(**kwargs)
    
  def to_json(self):
    r = super().to_json()
    if hasattr(self, 'user'):
      r.update({'user': self.user.to_json()})
    return r