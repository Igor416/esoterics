from bot.util import Update, PhotoReply, ReplyKeyboardMarkup, KeyboardButton
from user.models import User
from esoterics.settings import CHAT_ID

def send_answer(update: Update) -> PhotoReply:
  photo = sorted(update.message.photo, key=lambda el: el.file_size, reverse=True)[0]
  try:
    id, answer = update.message.caption.split(' ', 1)
  except:
    id, answer = CHAT_ID, update.message.caption
  user = User.objects.get(id=id)
  user.questions -= 1
  user.save()
  photo_reply = PhotoReply(
    chat_id=id,
    photo=photo.file_id,
    caption=answer,
    reply_markup=ReplyKeyboardMarkup(keyboard=[
      [KeyboardButton(text='Задать другой вопрос'), KeyboardButton(text='Проверить баланс')],
    ], is_persistent=True, resize_keyboard=True, one_time_keyboard=True),
  )
  return photo_reply