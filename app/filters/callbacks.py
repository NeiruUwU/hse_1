from typing import Literal, Optional
from aiogram.filters.callback_data import CallbackData

from app.models import Game


class GameCallback(CallbackData, prefix='game_callback'):
    state: Literal["start", "next-q", "finish", "cancel", "continue"] = 'start'
    question_id: Optional[str|int] = None
    answer_id: Optional[str|int] = None
    game: Optional[Game.Type] = None
    
class RatingCallback(CallbackData, prefix='rating_callback'):
    state: Literal["show", "cancel"]