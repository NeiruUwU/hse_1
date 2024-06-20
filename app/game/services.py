from app.models import Game, User, Question, Answer, Rating
from tortoise.contrib.sqlite.functions import Random
from tortoise.models import QuerySet

from .models import GameStep
import random

class GameService():
    game: Game
    player: User
    
    def __init__(self, game: Game, player: User):
        self.game = game
        self.player = player
    
    async def get_step(self) -> GameStep|None:
        question = await self.rand_question()
        if question is None:
            return None
        options = await self.rand_options()
        options.append(question.answer)
        random.shuffle(options)
        return GameStep(
            question=question,
            answer=question.answer,
            options=options,
        )
        
    async def answer_question(self, question: Question, answer: Answer) -> bool:
        status = question.answer.id == answer.id
        rating = await Rating.filter(game=self.game, user=self.player).first()
        rating = rating or await Rating.create(game=self.game, user=self.player)
        if status:
            rating.amount += 5
        else:
            rating.amount = max(rating.amount - 5, 0)
        await rating.save()
        return status
    
    async def rand_options(self, limit: int = 4) -> list[Answer]:
        query = Answer.filter(game_id=self.game.id)
        query = query.annotate(order=Random()).order_by('order')
        random_options = await query.limit(limit-1).all()
        return random_options
        
    async def rand_question(self) -> Question|None:
        query = Question.filter().prefetch_related('answer')
        query = query.filter(users__id__not=self.player.id)
        query = query.filter(game__id=self.game.id)
        query = query.annotate(order=Random()).order_by('order')
        random_question = await query.first()
        
        if random_question is None:
            questions_to_remove = await self.player.questions.filter(game_id=self.game.id).only('id')
            await self.player.questions.remove(*questions_to_remove)
        else:
            await random_question.users.add(self.player)

        return random_question
        
    