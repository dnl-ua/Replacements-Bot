import asyncio
from bot import bot
from config import TOKEN, CHANNEL_ID, IMAGE_PATH

async def send():
        await bot.send_photo(CHANNEL_ID, photo=open(IMAGE_PATH, 'rb'))

asyncio.run(send())
