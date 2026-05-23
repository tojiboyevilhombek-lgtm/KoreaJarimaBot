import logging
import os
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '7849691664:AAHscZX15aRK-mK8JRDPDfJk3xjbIJdxcXY'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Bot ishga tushdi va ulanish o'rnatildi!")

# Render uchun muhim: PORT sozlami
if __name__ == '__main__':
    # Render'da "Web Service" sifatida ishlash uchun 'skip_updates=True' juda muhim
    executor.start_polling(dp, skip_updates=True)
