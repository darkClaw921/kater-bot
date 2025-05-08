from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile
import os

from config import BOT_NAME, COMPANY_NAME
from utils.states import UserState
from utils.photo import get_photo_path

router = Router()


async def send_welcome(message: Message, state: FSMContext) -> None:
    """
    Обработчик команды /start
    """
    await state.clear()  # Очищаем состояние пользователя
    
    # Отправляем приветственное сообщение с фото
    welcome_text = (
        f"Алоха, любитель волн. Рады приветствовать тебя на канале {COMPANY_NAME}. Я "
        f"помощник команды – мое имя «{BOT_NAME}».\n\n"
        f"Добро пожаловать NA BOARD, мы с радостью откроем для тебя мир вейксерфинга и вейкбординга. Наша "
        f"команда - это профессионалы своего дела. Давай знакомится. Как твоё имя? Сколько тебе лет?"
    )
    
    # Получаем путь к фотографии приветствия
    photo_path = get_photo_path("welcome")
    
    if photo_path and os.path.exists(photo_path):
        # Отправляем фото с подписью
        photo = FSInputFile(photo_path)
        await message.answer_photo(photo=photo, caption=welcome_text)
    else:
        # Если фото не найдено, отправляем просто текст
        await message.answer(welcome_text)
        
    # Устанавливаем следующее состояние - ожидание имени и возраста
    await state.set_state(UserState.waiting_for_name_age)


def register_start_handlers(router: Router) -> None:
    """
    Регистрирует обработчики для начала работы с ботом
    """
    router.message.register(send_welcome, Command("start")) 