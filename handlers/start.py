from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from config import BOT_NAME, COMPANY_NAME
from utils.states import UserState

router = Router()


async def send_welcome(message: Message, state: FSMContext) -> None:
    """
    Обработчик команды /start
    """
    await state.clear()  # Очищаем состояние пользователя
    
    # Отправляем приветственное сообщение
    welcome_text = (
        f"Алоха, любитель волн. Рады приветствовать тебя в наше клубе {COMPANY_NAME}. Я "
        f"помощник команды – мое имя «{BOT_NAME}»\n\n"
        f"Мы с радостью откроем для тебя мир вейксерфинга и вейкбординга. Наша команда - это профессионалы "
        f"своего дела. Давай знакомится. Как твоё имя? Сколько тебе лет?"
    )
    
    await message.answer(welcome_text)
    await state.set_state(UserState.waiting_for_name_age)


def register_start_handlers(router: Router) -> None:
    """
    Регистрирует обработчики для начала работы с ботом
    """
    router.message.register(send_welcome, Command("start")) 