from app.models import Game, Answer, Question, OptionPivot

SCHEMA_COLOR = [
    {
        "img_path": "media/colors/1.png",
        "answer": "Абрикосовый",
        "options": [
            "Агатовый", 
            "Алый",
        ],
    },{
        "img_path": "media/colors/2.png",
        "answer": "Алый",
        "options": [
            "Красный", 
            "Амарантовый",
        ],
    },{
        "img_path": "media/colors/3.png",
        "answer": "Амарантовый",
        "options": [
            "Алый", 
            "Красный",
        ],
    },{
        "img_path": "media/colors/4.png",
        "answer": "Аметистовый",
        "options": [
            "Васильковый", 
            "Фиолетовый",
        ],
    },{
        "img_path": "media/colors/5.png",
        "answer": "Васильковый",
        "options": [
            "Голубой", 
            "Небесный",
        ],
    },{
        "img_path": "media/colors/6.png",
        "answer": "Изумруд",
        "options": [
            "Зелёный", 
            "Мятный",
        ],
    },{
        "img_path": "media/colors/7.png",
        "answer": "Индиго",
        "options": [
            "Голубой", 
            "Фиолетовый",
        ],
    },{
        "img_path": "media/colors/8.png",
        "answer": "Кирпичный",
        "options": [
            "Охра", 
            "Медный",
        ],
    },{
        "img_path": "media/colors/9.png",
        "answer": "Коралловый",
        "options": [
            "Оранжевый", 
            "Алый",
        ],
    },{
        "img_path": "media/colors/10.png",
        "answer": "Лиловый",
        "options": [
            "Розовый", 
            "Агатовый",
        ],
    },{
        "img_path": "media/colors/11.png",
        "answer": "Мятный",
        "options": [
            "Аквамарин", 
            "Ниагара",
        ],
    },{
        "img_path": "media/colors/12.png",
        "answer": "Оливковый",
        "options": [
            "Зелёный", 
            "Болотный",
        ],
    },{
        "img_path": "media/colors/13.png",
        "answer": "Маренго",
        "options": [
            "Оникс", 
            "Алебастр",
        ],
    },{
        "img_path": "media/colors/14.png",
        "answer": "Ниагара",
        "options": [
            "Ирис", 
            "Сапфировый",
        ],
    },{
        "img_path": "media/colors/15.png",
        "answer": "Охра",
        "options": [
            "Оранжевый", 
            "Кармин",
        ],
    },{
        "img_path": "media/colors/16.png",
        "answer": "Медный",
        "options": [
            "Сангина", 
            "Кирпич",
        ],
    },{
        "img_path": "media/colors/17.png",
        "answer": "Одуванчиковый",
        "options": [
            "Янтарь", 
            "Жёлтый",
        ],
    },{
        "img_path": "media/colors/18.png",
        "answer": "Пурпурный",
        "options": [
            "Фиолетовый", 
            "Алебастр",
        ],
    },{
        "img_path": "media/colors/19.png",
        "answer": "Алебастр",
        "options": [
            "Бежевый", 
            "Ниагара",
        ],
    },{
        "img_path": "media/colors/20.png",
        "answer": "Аквамарин",
        "options": [
            "Ниагара", 
            "Мятный",
        ],
    },{
        "img_path": "media/colors/21.png",
        "answer": "Кармин",
        "options": [
            "Кирпичный", 
            "Красный",
        ],
    },{
        "img_path": "media/colors/22.png",
        "answer": "Оникс",
        "options": [
            "Маренго", 
            "Индиго",
        ],
    },{
        "img_path": "media/colors/23.png",
        "answer": "Ирис",
        "options": [
            "Сапфировый", 
            "Индиго",
        ],
    },{
        "img_path": "media/colors/24.png",
        "answer": "Сангина",
        "options": [
            "Красный", 
            "Кирпичный",
        ],
    },{
        "img_path": "media/colors/25.png",
        "answer": "Цитрон",
        "options": [
            "Янтарь", 
            "Одуванчиковый",
        ],
    },{
        "img_path": "media/colors/26.png",
        "answer": "Янтарь",
        "options": [
            "Жёлтый", 
            "Одуванчиковый",
        ],
    },{
        "img_path": "media/colors/27.png",
        "answer": "Сапфировый",
        "options": [
            "Индиго", 
            "Синий",
        ],
    },
]


SCHEMA_FONT = [
    {
        "img_path": "media/fonts/4484.png",
        "answer": "Пиксельный",
        "options": [
            "Рукописный", 
            "Моноширинный",
            "Гротеск",
            "Антиква",
            "Готика",
        ],
    }, {
        "img_path": "media/fonts/4485.png",
        "answer": "Пиксельный",
        "options": [
            "Рукописный", 
            "Моноширинный",
            "Гротеск",
            "Антиква",
            "Готика",
        ],
    }, {
        "img_path": "media/fonts/4486.png",
        "answer": "Рукописный", 
        "options": [
            "Пиксельный",
            "Моноширинный",
            "Гротеск",
            "Антиква",
            "Готика",
        ],
    }, {
        "img_path": "media/fonts/4487.png",
        "answer": "Рукописный", 
        "options": [
            "Пиксельный",
            "Моноширинный",
            "Гротеск",
            "Антиква",
            "Готика",
        ],
    }, {
        "img_path": "media/fonts/4488.png",
        "answer": "Антиква", 
        "options": [
            "Пиксельный",
            "Моноширинный",
            "Гротеск",
            "Антиква",
            "Готика",
        ],
    }, {
        "img_path": "media/fonts/4489.png",
        "answer": "Антиква",
        "options": [
            "Рукописный", 
            "Пиксельный",
            "Моноширинный",
            "Гротеск",
            "Готика",
        ],
    }, {
        "img_path": "media/fonts/4490.png",
        "answer": "Рукописный", 
        "options": [
            "Пиксельный",
            "Моноширинный",
            "Гротеск",
            "Антиква",
            "Готика",
        ],
    }, {
        "img_path": "media/fonts/4491.png",
        "answer": "Рукописный",
        "options": [
            "Пиксельный",
            "Моноширинный",
            "Готика",
            "Антиква",
            "Гротеск",
        ],
    }, {
        "img_path": "media/fonts/4492.png",
        "answer": "Гротеск",
        "options": [
            "Пиксельный",
            "Моноширинный",
            "Рукописный",
            "Антиква",
            "Готика",
        ],
    }, {
        "img_path": "media/fonts/4493.png",
        "answer": "Гротеск",
        "options": [
            "Пиксельный",
            "Моноширинный",
            "Рукописный", 
            "Антиква",
            "Готика",
        ],
    }, {
        "img_path": "media/fonts/4494.png",
        "answer": "Гротеск",
        "options": [
            "Пиксельный",
            "Моноширинный",
            "Гротеск",
            "Рукописный", 
            "Антиква",
            "Готика",
        ],
    }, {
        "img_path": "media/fonts/4495.png",
        "answer": "Готика",
        "options": [
            "Пиксельный",
            "Моноширинный",
            "Гротеск",
            "Рукописный", 
            "Антиква",
            "Гротеск",
        ],
    }
]

async def games_seed():
    await _truncate_games()
    await game_color_seed()
    await game_font_seed()

async def game_color_seed():
    game: Game = await Game.update_or_create(
        name="Что за цвет?",
        code=Game.Type.COLOR.value)
    await _setting_game(game[0], SCHEMA_COLOR)

async def game_font_seed():
    game: Game = await Game.update_or_create(
        name="Что за шрифт?",
        code=Game.Type.FONT.value)
    await _setting_game(game[0], SCHEMA_FONT)
    
async def _setting_game(game: Game, schema: list):
    for question in schema:
        new_answer = await Answer.update_or_create(
            name=question.get("answer"),
            game=game
        )
        new_question = await Question.create(
            name=question.get("name"),
            img_path=question.get("img_path"),
            game_id=game.id,
            answer=new_answer[0]
        )
        for option in question.get("options", []):
            option = await Answer.update_or_create(
                name=option,
                game=game
            )
            await OptionPivot.update_or_create(question=new_question, answer=option[0])

async def _truncate_games():
    await Game.filter().delete()