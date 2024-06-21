from aiogram import Router, F  # Импортируем Router для создания роутинга и F для фильтрации
from aiogram.filters.callback_data import CallbackQuery  # Импорт для обработки коллбэков
from aiogram.types import BufferedInputFile, InlineKeyboardMarkup, InlineKeyboardButton  # Импортируем типы данных для работы с Telegram
from aiogram.exceptions import TelegramBadRequest  # Импортируем исключение для обработки ошибок Telegram API

from app.filters.callbacks import GameCallback  # Импортируем пользовательские коллбэки
from app.modules.game import GameService  # Импортируем сервис для работы с игрой
from app.models import Game, User, Answer, Question  # Импортируем модели данных

router = Router(name="GameCallbacks")  # Создаем роутер с именем "GameCallbacks"

# Обработчики коллбэков с состояниями "start" и "next-q" для GameCallback
@router.callback_query(GameCallback.filter(F.state == "start"))
@router.callback_query(GameCallback.filter(F.state == "next-q"))
async def game_start_cb(callback_query: CallbackQuery, callback_data: dict | GameCallback, user: User):
    # Получаем игру по коду из коллбэк данных
    game = await Game.filter(code=callback_data.game.value).first()
    # Создаем сервис для игры с указанным пользователем
    service = GameService(game, user)
    
    old_answer = None
    old_answer_status = False
    # Если есть данные о предыдущем ответе, обрабатываем его
    if callback_data.answer_id:
        old_answer = await Answer.filter(id=callback_data.answer_id).first()
        old_question = await Question.filter(id=callback_data.question_id).prefetch_related('answer').first()
        if old_question:
            old_answer_status = await service.answer_question(question=old_question, answer=old_answer)
    # Текст для победителя
    winner_text = "Вы ответили верно и получили +5 баллов!" if old_answer_status else "Вы ответили не правильно\!"
    
    # Получаем следующий шаг викторины
    step = await service.get_step(max_options=4)
    
    option_buttons = []
    
    # Если шаг равен None, значит викторина закончилась
    if step is None:
        # Клавиатура для возвращения в меню
        markup = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Вернуться в меню", callback_data=GameCallback(state="cancel").pack())
            ],
        ])
        # Если был предыдущий ответ, пытаемся отредактировать сообщение
        if old_answer:
            try:
                await callback_query.message.edit_text(
                    f"Правильный ответ был: {old_question.answer.name}.\n\n{winner_text}", 
                    reply_markup=None
                )
            except TelegramBadRequest:
                pass

        await callback_query.message.answer("Вы прошли Викторину\!", reply_markup=markup)
    
    # Формируем кнопки для вариантов ответа
    for option in step.options:
        callback_data = GameCallback(
            state="next-q", 
            question_id=step.question.id, 
            answer_id=option.id,
            game=callback_data.game,
        )
        button = InlineKeyboardButton(text=option.name, callback_data=callback_data.pack())
        option_buttons.append([button])

    # Разбиваем кнопки на пары для компактного отображения
    for i in range(0, len(option_buttons), 2):
        option = option_buttons[i:i + 2]

    # Клавиатура с кнопкой для возврата в меню
    markup = InlineKeyboardMarkup(inline_keyboard=option_buttons + [
        [
            InlineKeyboardButton(text="Меню", callback_data=GameCallback(state="cancel").pack())
        ],
    ])

    # Открываем файл с изображением вопроса
    with open(step.question.img_path, "rb") as file:
        # Если был предыдущий ответ, пытаемся отредактировать сообщение
        if old_answer:
            try:
                await callback_query.message.edit_reply_markup(reply_markup=None)
                await callback_query.message.edit_caption(
                    caption=f"Правильный ответ был: {old_question.answer.name}.\n\n{winner_text}", 
                    reply_markup=None
                )
            except TelegramBadRequest:
                pass
        # Отправляем сообщение с изображением и клавиатурой вариантов ответа
        await callback_query.message.answer_photo(
            BufferedInputFile(file.read(), filename=step.question.img_path),
            caption="Отлично! Посмотрите на картинку и выберите один из вариантов снизу",
            reply_markup=markup
        )
    await callback_query.answer()  # Отвечаем на коллбэк, чтобы Telegram не показывал ошибку ожидания ответа
