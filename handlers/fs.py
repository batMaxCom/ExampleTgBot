from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile

router = Router()

@router.message(Command("send_photo"))
async def send_photo_command(message: Message):
    # Создаем объект файла для загрузки
    image_from_pc = FSInputFile("static/cat.jpeg")
    # Отправляем фото с подписью и форматированием
    await message.answer_photo(
        photo=image_from_pc,
        caption="<b>Вот ваш котик!</b> ᓚᘏᗢ\n\n"
                "<em>Этот котик был загружен с компьютера.</em>",
        parse_mode="HTML"
    )