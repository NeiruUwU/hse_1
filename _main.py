import database.db as db
import asyncio
from database.seed import games_seed

from app.models import User, Game
from app.game.services import GameService

async def main():
    await db.init()
    # await games_seed()
    user = await User.filter(username="john_doe").first() or await User.create(username="john_doe")
    game_color = await Game.filter(code="game_font").first()
    
    game = GameService(game_color, user)
    step = await game.get_step()
    if step is not None:
        print(await game.answer_question(step.question, step.options[0]))
    await db.shutdown()

if __name__ == '__main__':
    asyncio.run(main())