from aiogram import Router, types
from aiogram.filters.command import Command

router = Router()

@router.message(Command("menu"))
async def menu(message: types.Message):
    """Выводит меню команд"""
    text = (
        "<b>Меню возможностей:</b>\n\n"
        "<i>Этот бот демонстрирует:</i>\n"
        " - Отправку форматированного текста\n"
        " - Отправку изображений и документов\n\n"
        "Воспользуйтесь командой /send_photo, чтобы получить картинку.\n\n"
        "Больше информации о фреймворке вы найдете в "
        "<a href='https://aiogram.dev/'>документации aiogram 3</a>."
    )
    await message.answer(text, parse_mode="HTML")
