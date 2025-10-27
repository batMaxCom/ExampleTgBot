from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile

router = Router()

@router.message(Command("send_photo"))
async def send_photo_command(message: Message):
    # Создаем объект файла для загрузки
    image_from_pc = FSInputFile("static/cat.jpeg")
    # Отправляем фото с подписью и форматированием
    await message.answer_photo( #  аналогично answer_document, answer_audio, answer_video и т.д.
        photo=image_from_pc,
        caption="<b>Вот ваш котик!</b> ᓚᘏᗢ\n\n" # отвечает за текстовую подпись, которая будет отправлена вместе с изображением.
                "<em>Этот котик был загружен с компьютера.</em>",
        parse_mode="HTML"
    )


# Отправка документа
# doc_from_pc = FSInputFile("document.pdf")
# await message.answer_document(doc_from_pc, caption="Вот инструкция.")

# Отправка аудио
# audio_from_pc = FSInputFile("music.mp3")
# await message.answer_audio(audio_from_pc, caption="Вот ваш трек.")