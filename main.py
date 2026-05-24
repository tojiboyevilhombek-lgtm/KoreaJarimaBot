import os
from aiogram import Bot, Dispatcher, executor, types
from aiohttp import web
import os
TOKEN = os.getenv('API_TOKEN')
API_TOKEN = '8929835764:AAFrhg9VQAFXXJi2L7sDB6XEXNzAGQpgDuY'
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
