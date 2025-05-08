from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.faq import FAQ


def get_question_keyboard() -> InlineKeyboardMarkup:
    """
    Создает инлайн-клавиатуру для выбора вопроса из FAQ
    """
    # Создаем список кнопок из вопросов
    buttons = []
    
    # Добавляем кнопки с вопросами
    for key, item in FAQ.items():
        question = item["question"]
        # Обрезаем длинные вопросы для кнопки
        if len(question) > 60:
            question = question[:57] + "..."
            
        buttons.append([InlineKeyboardButton(
            text=question, 
            callback_data=f"faq_{key}"
        )])
    
    # Добавляем кнопку возврата в меню
    buttons.append([InlineKeyboardButton(text="Назад в меню", callback_data="back_to_menu")])
    
    # Создаем клавиатуру
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb 