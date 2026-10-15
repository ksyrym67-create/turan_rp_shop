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
bot=telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    kb=types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("🛒 Дүкен","👤 Профиль")
    bot.send_message(m.chat.id,"🔥 Turan RP Shop-қа қош келдің!",reply_markup=kb)

@bot.message_handler(func=lambda m: m.text=="🛒 Дүкен")
def shop(m):
    bot.send_message(m.chat.id,"🛒 Тауарлар жақында!")

bot.infinity_polling()
