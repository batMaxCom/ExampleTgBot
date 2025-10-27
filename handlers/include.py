import logging

from aiogram import Dispatcher
from handlers import start, test_type, echo

router_list = [
    start,
    test_type,
    echo
]


async def include_router(dp: Dispatcher):
    for router in router_list:
        if router:
            dp.include_router(router.router)
        else:
            logging.debug("Router is None")
