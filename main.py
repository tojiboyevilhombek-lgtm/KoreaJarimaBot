import os
from aiogram import Bot, Dispatcher, executor, types

# Railway'dagi Variable dan tokenni o'qiydi
API_TOKEN = os.getenv('API_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Assalomu alaykum! Bot ishlamoqda!")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("Men sizning xabaringizni oldim!")

if __name__ == '__main__':
    # Webhook emas, Polling ishlatamiz
    executor.start_polling(dp, skip_updates=True)
