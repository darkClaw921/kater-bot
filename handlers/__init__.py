from aiogram import Dispatcher

from .start import register_start_handlers
from .menu import register_menu_handlers
from .user_info import register_user_info_handlers
from .questions import register_questions_handlers

def register_all_handlers(dp: Dispatcher) -> None:
    # Регистрация всех обработчиков в правильном порядке
    register_start_handlers(dp)
    register_user_info_handlers(dp)
    register_menu_handlers(dp)
    register_questions_handlers(dp) 