import asyncio
import logging

from aiogram import Bot, Dispatcher
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import text

from app.config import config
from app.routers.common import router as router_common
from app.routers.form import router as router_form
from app.database import async_main

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def test_db_connection():
    try:
        engine = create_async_engine(config.DATABASE_URL, echo = False)
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
    logger.info("Бот запущен!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
