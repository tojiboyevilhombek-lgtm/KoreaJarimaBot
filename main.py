import os
import logging
from aiogram import Bot, Dispatcher, executor, types

# Loglarni yoqish (xatolarni ko'rish uchun)
logging.basicConfig(level=logging.INFO)

# Tokenni Railway'dagi Variable dan olamiz
API_TOKEN = os.getenv('API_TOKEN')

# Botni sozlash
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# /start buyrug'i uchun javob
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Assalomu alaykum! Bot ishlamoqda!")

if __name__ == '__main__':
    # Webhook emas, polling ishlatamiz (bu eng barqaror usul)
    executor.start_polling(dp, skip_updates=True)
