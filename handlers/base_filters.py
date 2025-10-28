from aiogram import Router, F

router = Router()

@router.message(F.photo)
async def filter_photo(message):
    await message.answer("Отличное фото! Спасибо.")

@router.message(F.sticker)
async def filter_sticker(message):
    await message.answer("Милый стикер!")

@router.message(F.voice)
async def filter_voice(message):
    await message.answer("У вам отличный голос!")

# Обработка любых текстовых сообщений
# @router.message(F.text)
