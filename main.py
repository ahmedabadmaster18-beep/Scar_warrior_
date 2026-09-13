import os
import telebot

BOT_TOKEN = os.environ.get("BOT_TOKEN")
ADMIN_ID = os.environ.get("ADMIN_IDS")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_cmd(message):
    bot.reply_to(message, "नमस्ते! आपका बॉट ऑनलाइन हो चुका है।")

bot.infinity_polling()
