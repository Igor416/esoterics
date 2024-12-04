from bot.util import Update, Reply, InlineKeyboardMarkup, InlineKeyboardButton
from user.models import User
from typing import Tuple

def show_balance(update: Update) -> Tuple[Reply]:
  user = User.objects.get(id=update.message.chat.id)
  reply = Reply(
    chat_id=update.message.chat.id,
    text=f'Вопросов на вашем балансе: {user.questions}. Вы всегда можете купить еще через приложение',
    reply_markup=InlineKeyboardMarkup(inline_keyboard=[
      [InlineKeyboardButton(text='Открыть приложение', url='https://t.me/matrix_md_bot/main')],
    ]),
  )
  return (reply,)