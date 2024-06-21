from app.models import Question, Answer
from pydantic import BaseModel
from typing import Optional

class GameStep(BaseModel):
    question: Optional[Question]
    answer: Optional[Answer]
    options: list[Answer]
    
    class Config:
        arbitrary_types_allowed = True