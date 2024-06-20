from tortoise import Tortoise

from os import getenv

async def init():
    await Tortoise.init(
        db_url=getenv('DB_URL'),  # URL для подключения к SQLite
        modules={'models': ['app.models']},    # Модули, содержащие определения моделей
    )
    await Tortoise.generate_schemas()  # Создание таблиц на основе определений моделей

async def shutdown():
    await Tortoise.close_connections()  # Закрытие соединений с базой данных
