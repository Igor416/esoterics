from typing import List
from .base import Base

class Chat(Base):
  id: int
  first_name: str
  last_name: str
  username: str

class PhotoSize(Base):
  file_id: str
  file_unique_id: str
  width: int
  height: int
  file_size: int

class Message(Base):
  message_id: int
  chat: Chat
  text: str
  photo: List[PhotoSize]
  caption: str
  
  def __init__(self, **kwargs):
    self.chat = Chat(**kwargs.pop('chat'))
    if 'photo' in kwargs:
      self.photo = [PhotoSize(**el) for el in kwargs.pop('photo')]
    super().__init__(**kwargs)
  
class PreCheckoutQuery(Base):
  id: str
  invoice_payload: str

class Update(Base):
  update_id: int
  message: Message
  pre_checkout_query: PreCheckoutQuery
  
  def __init__(self, **kwargs):
    if 'message' in kwargs:
      self.message = Message(**kwargs.pop('message'))
    if 'pre_checkout_query' in kwargs:
      self.pre_checkout_query = PreCheckoutQuery(**kwargs.pop('pre_checkout_query'))
    super().__init__(**kwargs)