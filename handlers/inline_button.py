# то, что цепляется непосредственно к сообщениям - инлайн-кнопки
from random import randint

from aiogram import Router, F, Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Command
from aiogram.types import Message,InlineKeyboardButton, CallbackQuery, InlineKeyboardMarkup


router = Router()

from aiogram.utils.keyboard import InlineKeyboardBuilder

@router.message(Command("inline_url"))
async def cmd_inline_url(message: Message, bot: Bot):
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(
        text="GitHub", url="https://github.com")
    )
    builder.row(InlineKeyboardButton(
        text="Оф. канал Telegram",
        url="tg://resolve?domain=telegram")
    )

    # Чтобы иметь возможность показать ID-кнопку,
    # У юзера должен быть False флаг has_private_forwards
    user_id = 123456789
    try:
        chat_info = await bot.get_chat(user_id) # Получаем инфу о юзере, если отсутсвует - исключение TelegramBadRequest(chat not found)
        if not chat_info.has_private_forwards:
            builder.row(InlineKeyboardButton(
                text="Какой-то пользователь",
                url=f"tg://user?id={user_id}")
            )
    except TelegramBadRequest as e:
        pass

    await message.answer(
        'Выберите ссылку',
        reply_markup=builder.as_markup(),
    )

@router.message(Command("random"))
async def cmd_random(message: Message):
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(
        text="Нажми меня",
        callback_data="random_value" # добавляем для обозначения функции обработки
        )
    )
    await message.answer(
        "Нажмите на кнопку, чтобы бот отправил число от 1 до 10",
        reply_markup=builder.as_markup()
    )

@router.callback_query(F.data == "random_value")
async def send_random_value(callback: CallbackQuery): # Инициализируем функцию обаботки
    await callback.message.answer(str(randint(1, 10)))
    await callback.answer( # отключить ожидание подтверждения callback (всплывающее окно)
        text="Спасибо, что воспользовались ботом!",
        show_alert=True
    )
    # или просто
    # await callback.answer()

# region ----------------------------------- Пример ----------------------------------------------
user_data = {}

def get_keyboard():
    """ Инициализация клавиатуры """
    buttons = [
        [
            InlineKeyboardButton(text="-1", callback_data="num_decr"),
            InlineKeyboardButton(text="+1", callback_data="num_incr")
        ],
        [InlineKeyboardButton(text="Подтвердить", callback_data="num_finish")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


async def update_num_text(message: Message, new_value: int):
    """ Редактирование текста сообщения """
    await message.edit_text(
        f"Укажите число: {new_value}",
        reply_markup=get_keyboard()
    )


@router.message(Command("numbers"))
async def cmd_numbers(message: Message):
    """ Указываем начальное значение и добавляем кнопки """
    user_data[message.from_user.id] = 0
    await message.answer("Укажите число: 0", reply_markup=get_keyboard())


@router.callback_query(F.data.startswith("num_")) # Фильтр по началу строки
async def callbacks_num(callback: CallbackQuery):
    user_value = user_data.get(callback.from_user.id, 0)
    action = callback.data.split("_")[1]

    if action == "incr":
        user_data[callback.from_user.id] = user_value+1
        await update_num_text(callback.message, user_value+1)
    elif action == "decr":
        user_data[callback.from_user.id] = user_value-1
        await update_num_text(callback.message, user_value-1)
    elif action == "finish":
        await callback.message.edit_text(f"Итого: {user_value}")

    await callback.answer()
# endregion ---------------------------------------------------------------------------------
