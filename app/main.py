import asyncio
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

from aiogram import Bot, Dispatcher

from app.config import config
from app.routers.common import router as router_common
from app.routers.form import router as router_form


async def main():
    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router_form)
    dp.include_router(router_common)
    logger.info("Бот запущен!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
