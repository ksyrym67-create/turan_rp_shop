import telebot
from telebot import types

TOKEN = "8847459600:AAHGumOVORInFOTMXxysYG4mG-SwH1BKsbc"
KASPI = "+77076836915"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(text="🛡️ КОМАНДА ПРОЕКТ - 1000 тг", callback_data="komanda"),
        types.InlineKeyboardButton(text="👮 Зам Основатель - 1200 тг", callback_data="zam"),
        types.InlineKeyboardButton(text="👑 Осн - 1500 тг", callback_data="osn"),
        types.InlineKeyboardButton(text="💳 Каспий Төлем", callback_data="kaspi")
    )
    bot.send_message(message.chat.id, f"🎮 TURAN RP Дүкені\n\n💳 Каспий: {KASPI}\n\nТауар таңда 👇", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "kaspi":
        txt = f"💳 *Каспиймен төлеу*\n\nНомер: `{KASPI}`\nТөлеген соң чекті осы ботқа жібер!"
    elif call.data == "komanda":
        txt = f"🛡️ *КОМАНДА ПРОЕКТ*\nБағасы: 1000 тг\n\n💳 Каспий: `{KASPI}`"
    elif call.data == "zam":
        txt = f"👮 *Зам Основатель*\nБағасы: 1200 тг\n\n💳 Каспий: `{KASPI}`"
    else:
        txt = f"👑 *Осн*\nБағасы: 1500 тг\n\n💳 Каспий: `{KASPI}`"
    
    bot.send_message(call.message.chat.id, txt, parse_mode="Markdown")

bot.infinity_polling()
