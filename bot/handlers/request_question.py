from bot.util import Update, Reply, InlineKeyboardMarkup, InlineKeyboardButton
from user.models import User
from typing import Tuple

def request_question(update: Update) -> Tuple[Reply]:
  user = User.objects.get(id=update.message.chat.id)
  reply = Reply(
    chat_id=update.message.chat.id,
    text='К сожелению, у вас недостаточно вопросов на балансе, вы можете купить еще через приложение',
    reply_markup=InlineKeyboardMarkup(inline_keyboard=[
      [InlineKeyboardButton(text='Открыть приложение', url='https://t.me/matrix_md_bot/main')],
    ]),
  )
  if user.questions > 0:
    reply = Reply(
      chat_id=update.message.chat.id,
      text='Напиши свой вопрос, чем конкретней формулировка, тем яснее ответ, например: спрашивай про конкретного человека, уточняй временные рамки (ближайший месяц, следующий год)',
    )
  return (reply,)