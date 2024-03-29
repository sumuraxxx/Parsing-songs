import asyncio

from aiogram import Dispatcher


from initialization import dp, bot
from Bot.handlers.handlers import router


def register_router(dp: Dispatcher) -> None:
    """"Register router"""
    dp.include_router(router)


async def main() -> None:
    """Entry point"""
    register_router(dp=dp)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('end')
