from typing import Literal, Optional
from aiogram.filters.callback_data import CallbackData


class GameCallback(CallbackData, prefix='game_callback'):
    state: Literal["start", "next-q", "finish", "cancel", "continue"] = 'start'
    question_id: Optional[str|int] = None
    answer_id: Optional[str|int] = None