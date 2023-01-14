# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import telebot
from cfg import *

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types = ['text', 'image'])
def text(message):
    bot.send_message(message.from_user.id, message.text)

bot.infinity_polling()