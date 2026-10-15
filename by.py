import telebot
from telebot import types

TOKEN = "8847459600:AAHGumOVORInFOTMXxysYG4mG-SwH1BKsbcЙ"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("🛒 Дүкен", "👤 Профиль")
    bot.send_message(m.chat.id, "🔥 Turan RP дүкеніне қош келдің!", reply_markup=kb)

@bot.message_handler(func=lambda m: m.text == "🛒 Дүкен")
def shop(m):
    bot.send_message(m.chat.id, "🛒 Тауарлар:\n💰 100k - 500тг\n👑 VIP - 1000тг\n\nАдмин: @admin")

bot.infinity_polling()
