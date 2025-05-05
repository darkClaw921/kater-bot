from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from utils.states import UserState
from keyboards.experience_kb import get_experience_keyboard
from keyboards.menu_kb import get_menu_keyboard

router = Router()


async def process_name_age(message: Message, state: FSMContext) -> None:
    """
    Обработчик получения имени и возраста пользователя
    """
    user_data = message.text
    
    # Сохраняем данные пользователя
    await state.update_data(name_age=user_data)
    
    # Отправляем следующий вопрос с клавиатурой выбора опыта
    await message.answer(
        "Рады знакомству, ответь еще на один вопрос, чтобы мы подобрали для тебя необходимые "
        "услуги и предложения, рассказали о команде, наших акциях и специальных предложениях.\n\n"
        "Ты уже катал за катером на вейксерфе или вейкборде? Сколько раз?",
        reply_markup=get_experience_keyboard()
    )
    
    # Устанавливаем следующее состояние
    await state.set_state(UserState.waiting_for_experience)


async def process_experience(message: Message, state: FSMContext) -> None:
    """
    Обработчик получения опыта катания пользователя
    """
    experience = message.text
    
    # Сохраняем данные об опыте пользователя
    await state.update_data(experience=experience)
    
    # Получаем все данные пользователя
    user_data = await state.get_data()
    name_age = user_data.get("name_age", "")
    
    # Отправляем сообщение с меню
    await message.answer(
        f"Благодарю тебя за ответ. Я подготовил для тебя меню, нажми на интересующий тебя вопрос и "
        f"запишись на каталку.",
        reply_markup=get_menu_keyboard()
    )
    
    # Устанавливаем состояние меню
    await state.set_state(UserState.menu)


def register_user_info_handlers(router: Router) -> None:
    """
    Регистрирует обработчики для получения информации о пользователе
    """
    router.message.register(process_name_age, UserState.waiting_for_name_age)
    router.message.register(process_experience, UserState.waiting_for_experience) 