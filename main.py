import os
from aiogram import Bot, Dispatcher, executor, types
from aiohttp import web

API_TOKEN = '7849691664:AAFWqkeB1i3eqJw57CuqOIRHp6QaOVQF6MA'
# Render beradigan portni olamiz
PORT = int(os.environ.get('PORT', 8080))

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Bot Webhook orqali ishga tushdi!")

async def on_startup(dp):
    # Telegramga botimiz qayerdaligini aytamiz
    await bot.set_webhook("https://korea-jarima-bot.onrender.com")

if __name__ == '__main__':
    # Webhook rejimida ishga tushiramiz
    executor.start_webhook(
        dispatcher=dp,
        webhook_path='/',
        on_startup=on_startup,
        skip_updates=True,
        host="0.0.0.0",
        port=PORT,
    )
