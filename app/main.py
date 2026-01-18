import asyncio
import logging

from aiogram import Bot, Dispatcher
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.config import config
from app.database import async_main
from app.routers.common import router as router_common
from app.routers.form import router as router_form
from app.routers.admin import router as router_admin

logging.basicConfig(level=config.LOG_LEVEL,
                    format='[%(asctime)s] - [%(name)s] - [%(levelname)s] - [%(message)s]')
logger = logging.getLogger(__name__)


async def test_db_connection():
    try:
        engine = create_async_engine(config.DATABASE_URL, echo=False)
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        logger.info("Connection established")
        await engine.dispose()

    except Exception as e:
        logger.error(f"Не удалось подключиться к БД: {e}")
        exit(1)


async def main():
    await async_main()
    await test_db_connection()

    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router_form)
    dp.include_router(router_common)
    dp.include_router(router_admin)
    logger.info("Бот запущен!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
