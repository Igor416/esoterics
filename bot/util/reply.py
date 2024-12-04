from typing import List
import json
from .base import Base

class InlineKeyboardButton(Base):
  text: str
  url: str

class KeyboardButton(Base):
  text: str

class InlineKeyboardMarkup(Base):
  inline_keyboard: List[List[InlineKeyboardButton]]
    
  def to_json(self):
    return json.dumps({
      'inline_keyboard': [[button.to_json() for button in arr] for arr in self.inline_keyboard]
    })

class ReplyKeyboardMarkup(Base):
  keyboard: List[List[KeyboardButton]]
  is_persistent: bool
  resize_keyboard: bool
  one_time_keyboard: bool
    
  def to_json(self):
    r = super().to_json()
    r.update({'keyboard': [[button.to_json() for button in arr] for arr in self.keyboard]})
    return json.dumps(r)

class HasReplyMarkup(Base):
  reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup
  
  def to_json(self):
    r = super().to_json()
    if hasattr(self, 'reply_markup'):
      r.update({'reply_markup': self.reply_markup.to_json()})
    return r
  
class Reply(HasReplyMarkup):
  chat_id: int
  text: str

class PhotoReply(HasReplyMarkup):
  chat_id: str
  photo: str
  caption: str