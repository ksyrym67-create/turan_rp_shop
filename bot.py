  import telebot
from telebot import types
import os
from threading import Thread
from http.server import HTTPServer, BaseHTTPRequestHandler

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot running")
    def log_message(self,a,b=None,c=None): return

def run():
    HTTPServer(("", int(os.environ.get("PORT",10000))), H).serve_forever()
Thread(target=run, daemon=True).start()

TOKEN="8847459600:AAHGumOVORInFOTMXxysYG4mG-SwH1BKsbc"
ADMIN="@TuranAdmin"
bot=telebot.TeleBot(TOKEN)

PRODUCTS = {
    "komanda": {"name":"🛡️ КОМАНДА ПРОЕКТ", "price":"1000 тг", "desc":"Проект командасына кіру. Админканың бастамасы!"},
    "zam": {"name":"👮 Зам Осн", "price":"1200 тг", "desc":"Зам Основатель. /ban /kick + барлық командалар!"},
    "osn": {"name":"👑 Осн", "price":"1500 тг", "desc":"Основатель! Сервердің толық басқаруы. Ең жоғары админка!"},
}

@bot.message_handler(commands=['start'])
def start(m):
    kb=types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("🛒 Дүкен","👤 Профиль")
    bot.send_message(m.chat.id,f"🔥 Turan RP-ға қош келдің, {m.from_user.first_name}!\n\n👑 Админка сатылымы ашық!\nТөменнен дүкенді бас 👇",reply_markup=kb)

@bot.message_handler(func=lambda m: m.text in ["🛒 Дүкен","Дүкен","🛒 Дуken"])
def shop(m):
    kb=types.InlineKeyboardMarkup(row_width=1)
    for k,v in PRODUCTS.items():
        kb.add(types.InlineKeyboardButton(f"{v['name']} - {v['price']}", callback_data=k))
    bot.send_message(m.chat.id,"🛒 **Turan RP - Админка Дүкен:**\nТауарды таңда:", reply_markup=kb, parse_mode="Markdown")

@bot.message_handler(func=lambda m: m.text in ["👤 Профиль","Профиль"])
def profile(m):
    bot.send_message(m.chat.id,f"👤 **Профилің:**\n\nID: `{m.from_user.id}`\nАты: {m.from_user.first_name}\n\nАдминка алу үшін дүкенге өт!", parse_mode="Markdown")

@bot.callback_query_handler(func=lambda c: True)
def buy(c):
    p = PRODUCTS.get(c.data)
    if not p: return
    kb=types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("💳 Сатып алу / Жазу", url=f"https://t.me/{ADMIN.replace('@','')}"))
    text=f"**{p['name']}**\n\n💵 Бағасы: {p['price']}\n📝 {p['desc']}\n\nСатып алу үшін админге жаз:\n{ADMIN}\n\nТөлем Kaspi / Halyk\nID-ң: `{c.from_user.id}`"
    bot.send_message(c.message.chat.id, text, reply_markup=kb, parse_mode="Markdown")
    bot.answer_callback_query(c.id)

bot.infinity_polling()
