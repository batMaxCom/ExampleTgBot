import logging

from aiogram import Dispatcher
from handlers import start, test_type, echo, base_filters, menu, fs, base_button, inline_button, callback_factory

# Порядок имеет значение, так как хэндлеры обрабатываются в порядке их добавления
handlers_list = [
    start,
    base_filters,
    test_type,
    fs,
    menu,
    base_button,
    inline_button,
    callback_factory,
    echo
]


async def include_router(dp: Dispatcher):
    routers = [handler.router for handler in handlers_list]
    dp.include_routers(*routers)
