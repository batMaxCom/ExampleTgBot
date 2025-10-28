from typing import List

from aiogram import Router, F
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.types import Message
from aiogram.filters import Command

from filters.chat_type import ChatTypeFilter
from filters.return_value import HasUsernamesFilter

router = Router()

# фильтр можно применить ко всему роутеру
# router.message.filter(ChatTypeFilter(chat_type=["group", "supergroup"]))


@router.message(
    ChatTypeFilter(chat_type=["group", "supergroup"]), # вызываем кастомный фильтр
    Command(commands=["dice"]),
)
async def cmd_dice_in_group(message: Message):
    await message.answer_dice(emoji=DiceEmoji.DICE)


@router.message(
    F.text,
    HasUsernamesFilter() # вызываем кастомный фильтр который возвращает значения
)
async def message_with_usernames(
        message: Message,
        usernames: List[str] # орпеделяем выозвращаемое значение фильтра
):
    await message.reply(
        f'Спасибо! Обязательно подпишусь на '
        f'{", ".join(usernames)}'
    )