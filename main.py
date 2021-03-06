import datetime
import logging
import sys
import time
from sgp30 import SGP30
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


sgp30 = SGP30()
sgp30.start_measurement()


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}.')


def get(update: Update, context: CallbackContext) -> None:
    result = sgp30.get_air_quality()
    update.message.reply_text(f'VOC: {result.total_voc} ppb\neCO2: {result.equivalent_co2} ppm')


def log_forever():

    logger = logging.getLogger('air-quality-logger')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler('measurement.csv')
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    while True:
        result = sgp30.get_air_quality()
        timestamp = datetime.datetime.now()
        logger.info(f'{timestamp},{result.equivalent_co2},{result.total_voc}')
        time.sleep(1.0)


def main():

    if len(sys.argv) != 2:
        raise ValueError('Please provide your Telegram bot API token as a command line parameter.')

    updater = Updater(sys.argv[1])

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('get', get))

    updater.start_polling()
    #updater.idle()
    log_forever()


if __name__ == '__main__':
    main()
