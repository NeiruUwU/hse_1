from aiogram import Router, F  # Импортируем Router для создания роутинга и F для фильтрации
from aiogram.filters import CommandStart, Command  # Импортируем фильтры для команд /start и /statistics
from aiogram.filters.callback_data import CallbackQuery  # Импорт для обработки коллбэков
from aiogram.types import Message, BotCommand, InlineKeyboardMarkup, InlineKeyboardButton  # Импортируем типы сообщений и клавиатуры

from app.filters.callbacks import GameCallback, RatingCallback  # Импортируем пользовательские коллбэки
from app.models import Game, User, Rating  # Импортируем модели данных

router = Router(name="CommandsRouter")  # Создаем роутер с именем "CommandsRouter"

# Обработчик для команды /start и коллбэков с состоянием "cancel" для GameCallback и RatingCallback
@router.message(CommandStart())
@router.callback_query(GameCallback.filter(F.state == "cancel"))
@router.callback_query(RatingCallback.filter(F.state == "cancel"))
async def start_command(message: Message):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Что за шрифт?", callback_data=GameCallback(state="start", game=Game.Type.FONT).pack()),
                InlineKeyboardButton(text="Что за цвет?", callback_data=GameCallback(state="start", game=Game.Type.COLOR).pack())
            ],
            [InlineKeyboardButton(text="Статистика", callback_data=RatingCallback(state="show").pack())]
        ]
    )
    if hasattr(message, "message"):  # Проверяем, есть ли атрибут "message" у объекта
        message = message.message  # Если есть, используем его вместо исходного сообщения
    await message.answer(f"Добро пожаловать в викторину\!",  # Отправляем приветственное сообщение
                         parse_mode="MarkdownV2", reply_markup=markup)

# Обработчик для команды /statistics и коллбэков с состоянием "show" для RatingCallback
@router.message(Command('statistics'))
@router.callback_query(RatingCallback.filter(F.state == "show"))
async def startistics(message: Message, user: User):  # Функция для вывода статистики
    users = await User.filter().prefetch_related('rating').all()  # Запрашиваем пользователей с их рейтингом, отсортированных по рейтингу
    text = ''  # Переменная для формирования текста статистики
    for user_ in users:  # Перебираем пользователей
        rating = await Rating.filter(user=user_).first()  # Получаем рейтинг пользователя
        amount = 0  # Устанавливаем начальное значение рейтинга
        if rating:
            amount = rating.amount  # Если у пользователя есть рейтинг, используем его
        is_me = '-> ' if user_.id == user.id else ''  # Помечаем текущего пользователя стрелочкой "->", если это он
        text += f"\n{is_me} {user_.username}: {amount}"  # Формируем строку статистики для текущего пользователя
        
    markup = InlineKeyboardMarkup(inline_keyboard=[  # Создаем клавиатуру для возврата в главное меню
        [
            InlineKeyboardButton(text="Вернуться в меню", callback_data=GameCallback(state="cancel").pack())
        ],
    ])
    if hasattr(message, "message"):  # Проверяем, есть ли атрибут "message" у объекта
        message = message.message  # Если есть, используем его вместо исходного сообщения
    await message.answer(f"{text}",  # Отправляем текст статистики
                        reply_markup=markup)
