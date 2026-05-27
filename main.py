import os
import asyncio
from aiogram import Bot, Dispatcher, types
from flask import Flask
from threading import Thread

# 1. إعداد البوت
API_TOKEN = os.getenv('TELEGRAM_TOKEN')
bot = Bot(token=API_TOKEN)
dp = Dispatcher()  # التغيير هنا: لم نعد نضع 'bot' داخل الأقواس

# 2. كود الـ Keep-alive
app = Flask(__name__)

@app.route('/')
def home():
    return "Hermes is working!"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

# 3. وظيفة البوت
@dp.message() # التغيير هنا: بدل message_handler()
async def echo(message: types.Message):
    await message.answer("Hermes here! كيف يمكنني مساعدتك اليوم؟")

# 4. تشغيل البوت والخادم
async def main():
    Thread(target=run_flask, daemon=True).start()
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
