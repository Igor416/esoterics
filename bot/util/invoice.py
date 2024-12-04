from typing import List
import json
from .base import Base

class LabeledPrice(Base):
  label: str
  amount: int

class Invoice(Base):
  chat_id: int
  title: str
  description: str
  payload: str
  provider_token: str
  currency: str
  prices: List[LabeledPrice]
    
  def to_json(self):
    r = super().to_json()
    if hasattr(self, 'prices'):
      r.update({'prices': json.dumps([el.to_json() for el in self.prices])})
    return r
  
class PreCheckoutQueryAnswer(Base):
  pre_checkout_query_id: str
  ok: bool