from bot.models import Transaction
from bot.util import Update, PreCheckoutQueryAnswer, Reply, ReplyKeyboardMarkup, KeyboardButton

def answer_pre_checkout_query(update: Update) -> PreCheckoutQueryAnswer:
  answer = PreCheckoutQueryAnswer(
    pre_checkout_query_id=update.pre_checkout_query.id,
    ok=True
  )
  tr = Transaction.objects.get(id=update.pre_checkout_query.id)
  tr.finalised=True
  tr.user.questions += tr.amount
  tr.save()
  reply = Reply(
    chat_id=update.message.chat.id,
    text=f'Теперь у тебя вопросов на балансе: ({tr.user.questions}). Можешь задать их сейчас, нажав на кнопку "Задать вопрос" или в любое другое время, введя команду (просто впиши slash: /, в текстовое поле и выбери нужную)',
    reply_markup=ReplyKeyboardMarkup(keyboard=[
      [KeyboardButton(text='Задать вопрос')]
    ], is_persistent=True, resize_keyboard=True, one_time_keyboard=True),
  )
  return (answer, reply)