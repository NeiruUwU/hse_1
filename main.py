import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv

from app.handlers.callbacks import game
from app.handlers.texts import commands

import database.db as db
import asyncio
from database.seed import games_seed

from app.models import User, Game
from app.game.services import GameService

load_dotenv('.env')

bot = Bot(getenv("BOT_TOKEN"))
dp = Dispatcher()

dp.include_router(commands.router)
dp.include_router(game.router)

async def main():
    await db.init()
    await games_seed()
    # await bot.delete_webhook()
    await dp.start_polling(bot)
    await db.shutdown()

if __name__ == "__main__":
    asyncio.run(main())
    # asyncio.run(dp.start_polling(bot, skip_updates=True))