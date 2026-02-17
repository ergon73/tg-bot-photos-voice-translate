"""Точка входа бота."""

import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from .config import BOT_TOKEN
from .handlers import router

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


async def main() -> None:
    if not BOT_TOKEN:
        logger.error("BOT_TOKEN not set. Create .env from .env.example")
        sys.exit(1)
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties())
    dp = Dispatcher()
    dp.include_router(router)
    logger.info("Bot starting...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
