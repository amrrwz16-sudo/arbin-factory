import os
import asyncio
from aiogram import Bot, Dispatcher, types
from flask import Flask
from threading import Thread

# 1. إعداد البوت
API_TOKEN = os.getenv('TELEGRAM_TOKEN')
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# 2. كود الـ Keep-alive (لضمان بقاء البوت يعمل 24 ساعة)
app = Flask(__name__)

@app.route('/')
def home():
    return "Hermes is working!"

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

# 3. وظيفة البوت الأساسية (يرد على أي رسالة بـ "Hermes here!")
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("Hermes here! كيف يمكنني مساعدتك اليوم؟")

# 4. تشغيل البوت والخادم معاً
if __name__ == '__main__':
    # تشغيل خادم الويب في خلفية منفصلة
    Thread(target=run_flask).start()
    # تشغيل البوت
    asyncio.run(dp.start_polling(dp))
