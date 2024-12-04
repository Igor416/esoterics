from bot.util import Update, Reply, InlineKeyboardMarkup, InlineKeyboardButton
from user.models import User
from typing import Tuple

def start(update: Update) -> Tuple[Reply]:
  user = User.objects.filter(id=update.message.chat.id)
  if not user.exists():
    User.objects.create(**{field: getattr(update.message.chat, field) for field in update.message.chat.fields})
  reply = Reply(
    chat_id=update.message.chat.id,
    text='Привет, переходи по ссылке и запускай приложение! https://t.me/matrix_md_bot/main',
    reply_markup=InlineKeyboardMarkup(inline_keyboard=[
      [InlineKeyboardButton(text='Открыть приложение', url='https://t.me/matrix_md_bot/main')],
      [InlineKeyboardButton(text='Подписаться на канал', url='https://t.me/tarology_esoterics')],
    ]),
  )
  return (reply,)