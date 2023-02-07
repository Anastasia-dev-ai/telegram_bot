# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import telebot
from io import BytesIO
from cfg import *

bot = telebot.TeleBot(TOKEN)

from kandinsky2 import get_kandinsky2
model = get_kandinsky2('cpu', task_type='text2img')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет ✌️ Введи текстовое описание картинки")


@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.from_user.id, 'минуточку')
    print(message.text)
    images = model.generate_text2img(message.text, batch_size=4, h=512, w=512, num_steps=75,
                                     denoised_type='dynamic_threshold', dynamic_threshold_v=99.5,
                                     sampler='ddim_sampler', ddim_eta=0.01, guidance_scale=10)

    img = BytesIO()
    img.name = 'image.jpeg'
    images[1].save(img, 'JPEG')
    img.seek(0)
    bot.send_photo(message.from_user.id, img)


bot.infinity_polling()