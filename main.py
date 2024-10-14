import asyncio

from aiogram import Bot, Dispatcher

from app.handlers.user import user
from config import TOKEN_API

async def main() -> None:
    bot = Bot(token=TOKEN_API)
    dp = Dispatcher()
    dp.include_router(router=user)

    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped!")