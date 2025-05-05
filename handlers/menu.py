from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from keyboards.question_kb import get_question_keyboard
from keyboards.menu_kb import get_menu_keyboard
from utils.states import UserState

router = Router()


async def process_menu_faq(callback: CallbackQuery, state: FSMContext) -> None:
    """
    Обработчик выбора раздела 'Часто задаваемые вопросы'
    """
    await callback.answer()
    await callback.message.edit_text(
        "Выберите интересующий вас вопрос:",
        reply_markup=get_question_keyboard()
    )
    await state.set_state(UserState.questions)


async def process_menu_wakesurfing(callback: CallbackQuery) -> None:
    """
    Обработчик выбора раздела 'Про вейксерфинг'
    """
    await callback.answer()
    wakesurfing_info = (
        "<b>Вейксерфинг</b> - это катание на специальной доске по волне, создаваемой катером.\n\n"
        "Вейксерфинг – это серфинг с искусственной волной, которую создает специализированный катер. "
        "Доска для вейксерфа похожа на доску для классического серфа, только меньше. "
        "Преимущество в том, что кататься можно в наших широтах, а не только в океане."
    )
    await callback.message.edit_text(wakesurfing_info, reply_markup=get_menu_keyboard())


async def process_menu_wakeboarding(callback: CallbackQuery) -> None:
    """
    Обработчик выбора раздела 'Про вейкбординг'
    """
    await callback.answer()
    wakeboarding_info = (
        "<b>Вейкбординг</b> - это водный вид спорта, сочетающий в себе элементы водных лыж, сноуборда, "
        "скейтборда и серфинга.\n\n"
        "Катер буксирует райдера, стоящего на доске, и развивает достаточную скорость, чтобы он мог "
        "подниматься в воздух и выполнять различные трюки, используя кильватерную волну катера как трамплин."
    )
    await callback.message.edit_text(wakeboarding_info, reply_markup=get_menu_keyboard())


async def process_menu_price(callback: CallbackQuery) -> None:
    """
    Обработчик выбора раздела 'Прайс'
    """
    await callback.answer()
    price_info = (
        "<b>Наши цены:</b>\n\n"
        "• Сет 30 минут - 5000 руб.\n"
        "• Сет 60 минут - 9000 руб.\n"
        "• Сет 90 минут - 12000 руб.\n\n"
        "• Инструктор - 1500 руб.\n"
        "• Фото/видео съемка - 2000 руб.\n\n"
        "При бронировании от 2-х сетов скидка 10%"
    )
    await callback.message.edit_text(price_info, reply_markup=get_menu_keyboard())


async def process_menu_team(callback: CallbackQuery) -> None:
    """
    Обработчик выбора раздела 'Команда'
    """
    await callback.answer()
    team_info = (
        "<b>Наша команда:</b>\n\n"
        "• Иван - капитан и инструктор с опытом 5+ лет\n"
        "• Алексей - капитан и инструктор с опытом 4+ лет\n"
        "• Мария - администратор и инструктор\n"
        "• Дмитрий - инструктор и фотограф\n\n"
        "Мы работаем, чтобы сделать ваш отдых незабываемым!"
    )
    await callback.message.edit_text(team_info, reply_markup=get_menu_keyboard())


async def process_menu_booking(callback: CallbackQuery) -> None:
    """
    Обработчик выбора раздела 'Записаться'
    """
    await callback.answer()
    booking_info = (
        "Для записи на каталку, пожалуйста, свяжитесь с нашим администратором:\n\n"
        "• Телефон: +7 (999) 123-45-67\n"
        "• Почта: booking@wake.iv\n\n"
        "Или оставьте заявку на нашем сайте: wake.iv/booking"
    )
    await callback.message.edit_text(booking_info, reply_markup=get_menu_keyboard())


def register_menu_handlers(router: Router) -> None:
    """
    Регистрирует обработчики для меню
    """
    router.callback_query.register(process_menu_faq, F.data == "menu_faq")
    router.callback_query.register(process_menu_wakesurfing, F.data == "menu_wakesurfing")
    router.callback_query.register(process_menu_wakeboarding, F.data == "menu_wakeboarding")
    router.callback_query.register(process_menu_price, F.data == "menu_price")
    router.callback_query.register(process_menu_team, F.data == "menu_team")
    router.callback_query.register(process_menu_booking, F.data == "menu_booking") 