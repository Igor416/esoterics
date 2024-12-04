from bot.util import Update, Reply, ReplyKeyboardMarkup, KeyboardButton
from esoterics.settings import CHAT_ID
from typing import Tuple

def answer_question(update: Update) -> Tuple[Reply]:
  reply_to_user = Reply(
    chat_id=update.message.chat.id,
    text='Вопрос отправлен! Скоро пришлем тебе ответ и фотку самих карт (вдруг ты по-другому их почувствуешь). Вопрос с баланса спишется только после того, как ты получишь ответ',
    reply_markup=ReplyKeyboardMarkup(keyboard=[
      [KeyboardButton(text='Задать другой вопрос'), KeyboardButton(text='Проверить баланс')],
    ], is_persistent=True, resize_keyboard=True, one_time_keyboard=True),
  )
  reply_to_me = Reply(
    chat_id=CHAT_ID,
    text=f'Поступил вопрос от пользователя {update.message.chat.id}. Вопрос: "{update.message.text}"'
  )
  return (reply_to_user, reply_to_me)