from typing import List
import json
from .base import Base

class MessageEntity(Base):
  type: str
  offset: int
  length: int

class InputMediaPhoto(Base):
  type: str
  media: str
  caption: str
  parse_mode: str
  caption_entities: List[MessageEntity]
  
  def to_json(self):
    r = super().to_json()
    if hasattr(self, 'caption_entities'):
      r.update({'caption_entities': [entity.to_json() for entity in self.caption_entities]})
    return r

class MediaGroup(Base):
  chat_id: str
  media: List[InputMediaPhoto]
  
  def to_json(self):
    r = super().to_json()
    if hasattr(self, 'media'):
      r.update({'media': json.dumps([el.to_json() for el in self.media])})
    return r