import os
from aiogram import Router, F
from aiogram.filters.callback_data import CallbackData, CallbackQuery
from aiogram.types import BufferedInputFile
from aiogram.types import Message, BotCommand, InlineKeyboardMarkup, InlineKeyboardButton

from app.filters.callbacks import GameCallback


router = Router(name="GameCallbacks")


@router.callback_query(GameCallback.filter(F.state == "start"))
async def game_start_cb(callback_query: CallbackQuery, callback_data: GameCallback):
    # Buttons
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            "1. Answer one", 
            callback_data=GameCallback(state="next-q", question_id=1, answer_id=1).pack()
            )],
        [InlineKeyboardButton("2. Answer two", callback_data=GameCallback(state="next-q", question_id=1, answer_id=2).pack())],
        [InlineKeyboardButton("3. Answer three", callback_data=GameCallback(state="next-q", question_id=1, answer_id=3).pack())],
        [InlineKeyboardButton("4. Answer four", callback_data=GameCallback(state="next-q", question_id=1, answer_id=4).pack())],
        [InlineKeyboardButton("Cancel", callback_data=GameCallback(state="cancel").pack())],
    ])

    # Files
    with open("files/image_stub.jpg", "rb") as file:
        await callback_query.message.answer_photo(
            BufferedInputFile(file.read(), filename="image_stub.jpg"),
            caption="Отлично! Внимательно прочитайте вопрос на картинке и выберите один из вариантов снизу", 
            reply_markup=markup
        )
    
    await callback_query.answer()