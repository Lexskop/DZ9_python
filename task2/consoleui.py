from telegram.ext import Updater, CallbackContext, Filters, MessageHandler
from telegram import Update
from config import TOKEN

def view_data(data, title, update: Update, context: CallbackContext):
    update.message.reply_text(f'{title} = {data}')

def input_data(update: Update, context: CallbackContext):
    update.message.reply_text('Через пробел: 1 - компл., 2 - рац.числа; первое число; второе число; операция')
    message = update.message.text.split(' ')
    data_type = message[0]
    left_value = message[1]
    right_value = message[2]
    oper = message[3]
    return data_type, left_value, right_value, oper

updater = Updater(TOKEN)
dispetcher = updater.dispatcher
message_handler = MessageHandler(Filters.text, input_data)
dispetcher.add_handler(message_handler)
print('Cервер запущен')
updater.start_polling()
updater.idle()