import asyncio
import config
import logging
from aiogram import Bot, Dispatcher
from handlers import setup_routers
from middlewares.middleware import LoggingMiddleware

dp = Dispatcher()
dp.message.middleware(LoggingMiddleware())
setup_routers(dp)


# Run the bot
async def main() -> None:
    bot = Bot(token=config.TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        filename="logs/bot.log",  # ⚡ лог будет храниться в папке logs
        filemode="a",
        format="%(asctime)s - [%(levelname)s] - %(message)s",
        encoding="utf-8",
    )
    asyncio.run(main())
