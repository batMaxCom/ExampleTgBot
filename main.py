import asyncio
import logging
import os
import sys

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from dotenv import load_dotenv
from aiogram import Dispatcher, Bot

load_dotenv()
TOKEN = os.getenv("TOKEN")

# Все обработчики должны быть прикреплены к маршрутизатору (или диспетчеру)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    """Этот обработчик получает сообщения с `/start` командой"""
    await message.answer("Hello, World!")

@dp.message(Command("html"))
async def hello(message: Message):
    """Этот обработчик получает сообщения с `/http` командой и выводит HTML"""
    text = """
    <b>Жирный текст</b>
    <i>Курсивный текст</i>
    <u>Подчеркнутый текст</u>
    <s>Зачеркнутый текст</s>

    <b>Жирный <i>жирный курсив</i> внутри</b>
    <u>Подчеркнутый <s>подчеркнутый зачеркнутый</s> внутри</u>

    <a href="https://example.com">Встроенная ссылка</a>
    <code>Моноширинный текст (код)</code>

    <pre><code class="language-python">Блок кода
    с несколькими строками
    </code></pre>

    Не нужно экранировать символы!
    """
    await message.answer(text)

@dp.message(Command("markdown"))
async def hello(message: Message):
    """Этот обработчик получает сообщения с `/markdown` командой и выводит Markdown"""
    text = """
    *Жирный текст*
    _Курсивный текст_
    __Подчеркнутый__
    ~Зачеркнутый текст~

    *Жирный _жирный курсив_ внутри*
    __Подчеркнутый ~подчеркнутый зачеркнутый~ внутри__

    [Встроенная ссылка](https://example.com)
    [Текст кнопки](buttonurl:https://example.com)

    `Моноширинный текст (код)`
    ```python
    Блок кода
    с несколькими строками
    ``` 
    """
    await message.answer(text)

@dp.message()
async def echo_handler(message: Message):
    """Этот обработчик получает все остальные сообщения"""
    await message.answer(f"You said: {message.text}")

async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN_V2))
    """ Инициализация экземпляра бота с свойствами бота по умолчанию, которые будут переданы на все вызовы API"""
    await bot.delete_webhook(drop_pending_updates=True)     # Удаляем вебхук и пропускаем накопившиеся входящие сообщения
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
