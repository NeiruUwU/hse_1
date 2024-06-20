from app.models import Game, Answer, Question

SCHEMA_COLOR = [
    {
        "img_path": "game/media/example.py",
        "answer": "adafsasdf"
    },
    {
        "img_path": "game/media/example.py",
        "answer": "adafsasdf"
    },
    {
        "img_path": "game/media/example.py",
        "answer": "adafsasdf"
    },
    {
        "img_path": "game/media/example.py",
        "answer": "adafsasdf"
    },
    {
        "img_path": "game/media/example.py",
        "answer": "adafsasdf"
    },
    {
        "img_path": "game/media/example.py",
        "answer": "adafsasdf"
    },
]

SCHEMA_FONT = [
    {
        "img_path": "game/media/example.py",
        "answer": "1"
    },
    {
        "img_path": "game/media/example.py",
        "answer": "2"
    },
    {
        "img_path": "game/media/example.py",
        "answer": "3"
    },
    {
        "img_path": "game/media/example.py",
        "answer": "4"
    },
    {
        "img_path": "game/media/example.py",
        "answer": "5"
    },
    {
        "img_path": "game/media/example.py",
        "answer": "6"
    },
]

async def games_seed():
    # await _truncate_games()
    await game_color_seed()
    await game_font_seed()

async def game_color_seed():
    game: Game = await Game.update_or_create(
        name="Что за цвет?",
        code="game_color")
    await _setting_game(game[0], SCHEMA_COLOR)

async def game_font_seed():
    game: Game = await Game.update_or_create(
        name="Что за шрифт?",
        code="game_font")
    await _setting_game(game[0], SCHEMA_FONT)
    
async def _setting_game(game: Game, schema: list):
    for question in schema:
        new_answer = await Answer.create(
            name=question.get("answer"),
            game=game)
        await Question.create(
            name=question.get("name"),
            img_path=question.get("img_path"),
            game_id=game.id,
            answer=new_answer)

async def _truncate_games():
    await Game.filter().delete()