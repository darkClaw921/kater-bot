from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.faq import MENU_ITEMS


def get_menu_keyboard() -> InlineKeyboardMarkup:
    """
    Создает инлайн-клавиатуру для главного меню
    """
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=MENU_ITEMS["faq"], callback_data="menu_faq")],
            [InlineKeyboardButton(text=MENU_ITEMS["wakesurfing"], callback_data="menu_wakesurfing")],
            [InlineKeyboardButton(text=MENU_ITEMS["wakeboarding"], callback_data="menu_wakeboarding")],
            [InlineKeyboardButton(text=MENU_ITEMS["price"], callback_data="menu_price")],
            [InlineKeyboardButton(text=MENU_ITEMS["team"], callback_data="menu_team")],
            [InlineKeyboardButton(text=MENU_ITEMS["booking"], callback_data="menu_booking")],
        ]
    )
    return kb 