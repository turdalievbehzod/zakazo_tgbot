import asyncio
from aiogram import Bot, Dispatcher
from core.db_settings import execute_query
from core.models import *
from core.config import BOT_TOKEN
from handlers import start, user, admin

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

dp.include_router(start.router)
dp.include_router(user.router)
dp.include_router(admin.router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    execute_query(users)
    execute_query(products)
    execute_query(menu_products)
    execute_query(durations)
    execute_query(orders)

    asyncio.run(main())
