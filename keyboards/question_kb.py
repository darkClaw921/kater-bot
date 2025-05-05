from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.faq import FAQ


def get_question_keyboard() -> InlineKeyboardMarkup:
    """
    Создает инлайн-клавиатуру для выбора вопроса из FAQ
    """
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=FAQ["beginner"]["question"], callback_data="faq_beginner")],
            [InlineKeyboardButton(text=FAQ["equipment"]["question"], callback_data="faq_equipment")],
            [InlineKeyboardButton(text=FAQ["gift_certificates"]["question"], callback_data="faq_gift_certificates")],
            [InlineKeyboardButton(text=FAQ["subscriptions"]["question"], callback_data="faq_subscriptions")],
            [InlineKeyboardButton(text=FAQ["solo"]["question"], callback_data="faq_solo")],
            [InlineKeyboardButton(text=FAQ["capacity"]["question"], callback_data="faq_capacity")],
            [InlineKeyboardButton(text=FAQ["pets"]["question"], callback_data="faq_pets")],
            [InlineKeyboardButton(text=FAQ["weather"]["question"], callback_data="faq_weather")],
            [InlineKeyboardButton(text=FAQ["booking"]["question"], callback_data="faq_booking")],
            [InlineKeyboardButton(text="Назад в меню", callback_data="back_to_menu")],
        ]
    )
    return kb 