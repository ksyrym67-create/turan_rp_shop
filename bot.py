import telebot
from telebot import types

TOKEN = "8847459600:AAHGumOVORInFOTMXxysy"
KASPI_NUMBER = "+77076836915"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(text="🛡️ КОМАНДА ПРОЕКТ - 1000 тг", callback_data="komanda"),
        types.InlineKeyboardButton(text="👮 Зам Основатель - 1200 тг", callback_data="zam"),
        types.InlineKeyboardButton(text="👑 Осн - 1500 тг", callback_data="osn"),
        types.InlineKeyboardButton(text="💳 Каспийге төлеу", callback_data="kaspi"),
        types.InlineKeyboardButton(text="📞
