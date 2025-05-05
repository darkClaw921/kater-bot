from aiogram.fsm.state import State, StatesGroup


class UserState(StatesGroup):
    """Класс для хранения состояний пользователя"""
    # Состояния диалога
    waiting_for_name_age = State()
    waiting_for_experience = State()
    menu = State()
    questions = State() 