from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    """Этот обработчик получает сообщения с `/start` командой"""
    await message.answer("Hello, World!")