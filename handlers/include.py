import logging

from aiogram import Dispatcher
from handlers import start, test_type, echo, filters, menu, fs

# Порядок имеет значение, так как хэндлеры обрабатываются в порядке их добавления
handlers_list = [
    start,
    filters,
    test_type,
    fs,
    menu,
    echo
]


async def include_router(dp: Dispatcher):
    for handler in handlers_list:
        if handler:
            dp.include_router(handler.router)
        else:
            logging.debug("Router is None")
