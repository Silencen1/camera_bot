from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
BASE_URL = os.getenv("BASE_URL")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    user_id = message.chat.id
    camera_url = f"{BASE_URL}/camera?user_id={user_id}"
    await message.answer(f"📷 Kamerani yoqish uchun bosing:\n{camera_url}")

if __name__ == "__main__":
    executor.start_polling(dp)
