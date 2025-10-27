from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def echo_handler(message: Message):
    """Этот обработчик получает все остальные сообщения"""
    await message.answer(f"You said: {message.text}")