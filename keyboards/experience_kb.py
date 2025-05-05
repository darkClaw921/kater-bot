from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_experience_keyboard() -> ReplyKeyboardMarkup:
    """
    Создает клавиатуру для выбора опыта катания
    """
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Нет")],
            [KeyboardButton(text="Да")],
            [KeyboardButton(text="Больше 3-х раз")],
            [KeyboardButton(text="Уверено катаю")],
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
    )
    return kb 