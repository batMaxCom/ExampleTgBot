# то, что цепляется к низу экрана вашего устройства - обычные кнопки
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButtonPollType, \
    KeyboardButtonRequestUser, KeyboardButtonRequestChat
from aiogram.utils.keyboard import ReplyKeyboardBuilder

router = Router()

@router.message(Command("button"))
async def button(message: Message):
    """ Пример с кнопками"""
    kb = [ # составляем маасив кнопок
            [
                KeyboardButton(text="Кнопка 1"), # все запишутся в строку
                KeyboardButton(text="Кнопка 2"),
                KeyboardButton(text="Кнопка 3")

            ],
            [
                KeyboardButton(text="Кнопка 4"), # запишутся в новую строку
            ],
            [
                KeyboardButton(text="Кнопка 5"),
                KeyboardButton(text="Кнопка 6")
            ]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True, # для уменьшения кнопок к объекту клавиатуры
        input_field_placeholder="Выберите способ подачи" # заменит текст в пустой строке ввода, когда активна обычная клавиатура
    )
    await message.answer("Пример с кнопками", reply_markup=keyboard)

@router.message(F.text == "Кнопка 1")
async def button1(message: Message):
    await message.reply("Вы выбрали кнопку 1") # добавит ссылку на ответ пользователя

@router.message(F.text == "Кнопка 2")
async def button2(message: Message):
    await message.reply("Удаляю кнопки!", reply_markup=ReplyKeyboardRemove()) # удалит клавиатуру

@router.message(Command("reply_builder"))
async def reply_builder(message: Message):
    """
    add(<KeyboardButton>) — добавляет кнопку в память сборщика;
    adjust(int1, int2, int3...) — делает строки по int1, int2, int3... кнопок;
    as_markup() — возвращает готовый объект клавиатуры;
    button(<params>) — добавляет кнопку с заданными параметрами, тип кнопки (Reply или Inline) определяется автоматически.
    """
    builder = ReplyKeyboardBuilder()
    for i in range(1, 10):
        builder.add(KeyboardButton(text=str(i)))
    builder.adjust(4)
    await message.answer(
        "Пример с ReplyKeyboardBuilder",
        reply_markup=builder.as_markup(resize_keyboard=True)
    )

@router.message(Command("special_buttons"))
async def cmd_special_buttons(message: Message):
    """
    request_location - запросить геолокацию
    request_contact - запросить контакт
    request_poll - запросить опрос
    request_user - запросить пользователя
    request_chat - запросить чат

    """
    builder = ReplyKeyboardBuilder()
    # метод row позволяет явным образом сформировать ряд
    # из одной или нескольких кнопок. Например, первый ряд
    # будет состоять из двух кнопок...
    builder.row(
        KeyboardButton(text="Запросить геолокацию", request_location=True),
        KeyboardButton(text="Запросить контакт", request_contact=True)
    )
    # ... второй из одной ...
    builder.row(KeyboardButton(
        text="Создать викторину",
        request_poll=KeyboardButtonPollType(type="quiz"))
    )
    # ... а третий снова из двух
    builder.row(
        KeyboardButton(
            text="Выбрать премиум пользователя",
            request_user=KeyboardButtonRequestUser(
                request_id=1,
                user_is_premium=False
            )
        ),
        KeyboardButton(
            text="Выбрать супергруппу с форумами",
            request_chat=KeyboardButtonRequestChat(
                request_id=2,
                chat_is_channel=False,
                chat_is_forum=True
            )
        )
    )
    await message.answer(
        "Выберите действие:",
        reply_markup=builder.as_markup(resize_keyboard=True),
    )

# Примеры обработчиков на кнопки о геолокации и пользователе
@router.message(F.location)
async def on_location_shared(message: Message):
    await message.answer(
        (
            f"Latitude: {message.location.latitude}\n"
            f"Longitude: {message.location.longitude}"
        )
    )


@router.message(F.user_shared)
async def on_user_shared(message: Message):
    print(
        f"Request {message.user_shared.request_id}\n"
        f"User ID: {message.user_shared.user_id}"
    )