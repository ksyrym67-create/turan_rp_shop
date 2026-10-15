import telebot
from telebot import types

TOKEN = "8301432282:AAF3FfWk3zRjV1A5bT5y7x8z9a0b1c2d3e4f"
bot = telebot.TeleBot(TOKEN)

ADMIN_NUMBER = "+77076836915"

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(text="🛡️ КОМАНДА ПРОЕКТ - 1000 тг", callback_data="komanda"),
        types.InlineKeyboardButton(text="👮 Зам Основатель - 1200 тг", callback_data="zam"),
        types.InlineKeyboardButton(text="👑 Осн - 1500 тг", callback_data="osn"),
        types.InlineKeyboardButton(text="📞 Админмен байланыс", url=f"https://wa.me/77076836915")
    )
    bot.send_message(message.chat.id, f"🎮 *Turan RP Дүкеніне қош келдің!*\n\nТауар таңда:\nАдмин: {ADMIN_NUMBER}", parse_mode="Markdown", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "komanda":
        text = f"🛡️ *КОМАНДА ПРОЕКТ*\nБағасы: 1000 тг\n\nСатып алу үшін жаз:\n📞 {ADMIN_NUMBER}\nWhatsApp: https://wa.me/77076836915"
    elif call.data == "zam":
        text = f"👮 *Зам Основатель*\nБағасы: 1200 тг\n\nСатып алу үшін жаз:\n📞 {ADMIN_NUMBER}\nWhatsApp: https://wa.me/77076836915"
    elif call.data == "osn":
        text = f"👑 *Осн*\nБағасы: 1500 тг\n\nСатып алу үшін жаз:\n📞 {ADMIN_NUMBER}\nWhatsApp: https://wa.me/77076836915"
