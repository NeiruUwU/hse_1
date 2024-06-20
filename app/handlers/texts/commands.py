from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, BotCommand, InlineKeyboardMarkup, InlineKeyboardButton

from app.filters.callbacks import GameCallback

router = Router(name="CommandsRouter")


@router.message(CommandStart())
async def start_command(message: Message):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Начать викторину", callback_data=GameCallback(state="start").pack())]
    ])
    await message.answer(f"Добро пожаловать в викторину\!", 
                         parse_mode="MarkdownV2", reply_markup=markup)