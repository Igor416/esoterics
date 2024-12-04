from bot.util import Update, Reply
from typing import Tuple

def unknown(update: Update) -> Tuple[Reply]:
  reply = Reply(
    chat_id=update.message.chat.id,
    text='Не совсем тебя понял...'
  )
  return (reply,)