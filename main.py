import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '7849691664:AAHscZX15aRK-mK8JRDPDfJk3xjbIJdxcXY'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum! Korea Avto Jarima Botiga xush kelibsiz.")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(f"Siz yuborgan raqam: {message.text}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
