"""Основной файл запуска бота"""

from telebot import TeleBot, types
import config
from sched_run import run_on_time
import sys


bot = TeleBot(config.BTOKEN)


@bot.message_handler(commands=["zakaz"])
def send_first_message(message: types.Message):
    """Dummy"""
    txt = "Это функция заказ"
    bot.send_message(message.chat.id, txt)

@bot.message_handler(commands=['alarma'])
def stop():
    sys.exit(0)

def send_sched_message(txt):
    bot.send_message(chat_id=565035378, text=txt)


@bot.message_handler()
def send_echo_message(message: types.Message):
    """Dummy"""

    bot.send_message(message.chat.id, message.text)







if __name__ == "__main__":
    run_on_time()
    bot.infinity_polling(skip_pending=True)
