import os
import threading
import urllib.request
import logging
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN, URL, IMAGE_PATH


def download_image():
        url = URL
        urllib.request.urlretrieve(url, IMAGE_PATH)


logging.basicConfig(level=logging.INFO)

api_token = TOKEN
bot = Bot(token=api_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
        await message.reply("Чтобы получить список замен введите команду /send");


@dp.message_handler(commands=['send'])
async def send(message: types.Message):
        download_image()
        with open(IMAGE_PATH, 'rb') as photo:
                await message.reply_photo(photo)


if __name__ == '__main__':
        executor.start_polling(dp, skip_updates=True)
