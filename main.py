import asyncio
import logging
import os
import sys

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv
from aiogram import Dispatcher, Bot

from handlers.include import include_router

load_dotenv()
TOKEN = os.getenv("TOKEN")

# Все обработчики должны быть прикреплены к маршрутизатору (или диспетчеру)
dp = Dispatcher()

async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    """ Инициализация экземпляра бота с свойствами бота по умолчанию, которые будут переданы на все вызовы API"""
    await include_router(dp)
    await bot.delete_webhook(drop_pending_updates=True)     # Удаляем вебхук и пропускаем накопившиеся входящие сообщения
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
