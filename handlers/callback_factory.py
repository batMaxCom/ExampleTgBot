from contextlib import suppress
from typing import Optional

from aiogram import Router, F
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackData
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()
user_data = {}


class NumbersCallbackFactory(CallbackData, prefix="fabnum"):
    """Определение класса callback_data для кнопок"""
    action: str
    value: Optional[int] = None

def get_keyboard_fab():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="-2", callback_data=NumbersCallbackFactory(action="change", value=-2)
    )
    builder.button(
        text="-1", callback_data=NumbersCallbackFactory(action="change", value=-1)
    )
    builder.button(
        text="+1", callback_data=NumbersCallbackFactory(action="change", value=1)
    )
    builder.button(
        text="+2", callback_data=NumbersCallbackFactory(action="change", value=2)
    )
    builder.button(
        text="Подтвердить", callback_data=NumbersCallbackFactory(action="finish")
    )
    # Выравниваем кнопки по 4 в ряд, чтобы получилось 4 + 1
    builder.adjust(4)
    return builder.as_markup()

async def update_num_text_fab(message: Message, new_value: int):
    with suppress(TelegramBadRequest):
        await message.edit_text(
            f"Укажите число: {new_value}",
            reply_markup=get_keyboard_fab()
        )

@router.message(Command("numbers_fab"))
async def cmd_numbers_fab(message: Message):
    user_data[message.from_user.id] = 0
    await message.answer("Укажите число: 0", reply_markup=get_keyboard_fab())

# Исползуем как общий обработчик для всех NumbersCallbackFactory колбэков

# @router.callback_query(NumbersCallbackFactory.filter())
# async def callbacks_num_change_fab(
#         callback: CallbackQuery,
#         callback_data: NumbersCallbackFactory
# ):
#     # Текущее значение
#     user_value = user_data.get(callback.from_user.id, 0)
#     # Если число нужно изменить
#     if callback_data.action == "change":
#         user_data[callback.from_user.id] = user_value + callback_data.value
#         await update_num_text_fab(callback.message, user_value + callback_data.value)
#     # Если число нужно зафиксировать
#     else:
#         await callback.message.edit_text(f"Итого: {user_value}")
#     await callback.answer()

# Или, например, для каждого Action отдельно

# Нажатие на одну из кнопок: -2, -1, +1, +2
@router.callback_query(NumbersCallbackFactory.filter(F.action == "change"))
async def callbacks_num_change_fab(
        callback: CallbackQuery,
        callback_data: NumbersCallbackFactory
):
    # Текущее значение
    user_value = user_data.get(callback.from_user.id, 0)

    user_data[callback.from_user.id] = user_value + callback_data.value
    await update_num_text_fab(callback.message, user_value + callback_data.value)
    await callback.answer()


# Нажатие на кнопку "подтвердить"
@router.callback_query(NumbersCallbackFactory.filter(F.action == "finish"))
async def callbacks_num_finish_fab(callback: CallbackQuery):
    # Текущее значение
    user_value = user_data.get(callback.from_user.id, 0)

    await callback.message.edit_text(f"Итого: {user_value}")
    await callback.answer()