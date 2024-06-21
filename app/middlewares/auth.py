from aiogram import types
from aiogram.fsm.context import FSMContext
from app.models import User

from aiogram import BaseMiddleware
from aiogram.types import Message, Update

from typing import Callable, Dict, Any, Awaitable

async def get_user_from_username(
    handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
    event: Update,
    data: Dict[str, Any]
):
    # Получаем username из сообщения
    from_user = None
    if event.callback_query:
        from_user = event.callback_query.from_user
    elif event.message:
        from_user = event.message.from_user

    if from_user:
        # Ищем пользователя в базе данных по username
        user, created = await User.get_or_create(username=from_user.username)
        data['user'] = user
        
    # Сохраняем пользователя в состояние и передаем управление обработчику
    return await handler(event, data)