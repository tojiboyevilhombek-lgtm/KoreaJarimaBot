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

# Webhookni o'chirish funksiyasi
async def on_startup(dispatcher):
    await bot.delete_webhook()
    logging.info("Webhook o'chirildi va bot ishga tushdi!")

# /start buyrug'i uchun javob
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Assalomu alaykum! Bot ishlamoqda!")

if __name__ == '__main__':
    # Polling ishlatamiz
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
