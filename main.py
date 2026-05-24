import os
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = os.getenv('API_TOKEN')
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Bot ishlamoqda!")

if __name__ == '__main__':
    executor.start_polling(dp)
