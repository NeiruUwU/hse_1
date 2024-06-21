import asyncio  # Импорт модуля asyncio для асинхронной работы
from aiogram import Bot, Dispatcher  # Импорт классов Bot и Dispatcher из aiogram для работы с Telegram API
from dotenv import load_dotenv  # Импорт функции load_dotenv для загрузки переменных окружения
from os import getenv  # Импорт функции getenv для доступа к переменным окружения

# Импорт пользовательских обработчиков коллбэков и текстовых команд
from app.handlers.callbacks import game  
from app.handlers.texts import commands  

# Импорт middleware для аутентификации пользователя
from app.middlewares.auth import get_user_from_username  

import database.db as db  # Импорт модуля для работы с базой данных
from database.seed import games_seed  # Импорт функции для инициализации данных в базе

load_dotenv('.env')  # Загрузка переменных окружения из файла .env

bot = Bot(getenv("BOT_TOKEN"))  # Создание объекта бота с использованием токена из переменных окружения
dp = Dispatcher()  # Создание диспетчера для обработки входящих сообщений и коллбэков

dp.include_router(game.router)  # Включение роутера для обработки коллбэков игры
dp.include_router(commands.router)  # Включение роутера для обработки текстовых команд

dp.update.middleware.register(get_user_from_username)  # Регистрация middleware для аутентификации пользователя

async def main():
    await db.init()  # Инициализация соединения с базой данных
    await games_seed()  # Инициализация данных в базе (например, загрузка игр)
    await dp.start_polling(bot)  # Запуск бота с использованием long polling
    await db.shutdown()  # Закрытие соединения с базой данных при завершении работы бота

if __name__ == "__main__":
    asyncio.run(main())  # Запуск основной функции как асинхронной задачи при запуске скрипта
