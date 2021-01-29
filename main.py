import sys
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


if len(sys.argv) != 2:
    raise ValueError('Please provide your Telegram bot API token as a command line parameter.')

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def get(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'No data yet.')


updater = Updater(sys.argv[1])

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('get', get))

updater.start_polling()
updater.idle()