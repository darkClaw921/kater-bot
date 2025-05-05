from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from data.faq import FAQ
from keyboards.menu_kb import get_menu_keyboard
from keyboards.question_kb import get_question_keyboard
from utils.states import UserState

router = Router()


async def process_faq_question(callback: CallbackQuery) -> None:
    """
    Общий обработчик для всех FAQ вопросов
    """
    await callback.answer()
    
    # Получаем ключ вопроса из callback_data (обрезаем префикс "faq_")
    faq_key = callback.data.replace("faq_", "")
    
    if faq_key in FAQ:
        # Формируем ответ из вопроса и ответа
        response = f"<b>{FAQ[faq_key]['question']}</b>\n\n{FAQ[faq_key]['answer']}"
        
        # Отправляем ответ и клавиатуру с вопросами
        await callback.message.edit_text(
            response,
            reply_markup=get_question_keyboard()
        )
    else:
        # Если вопрос не найден, сообщаем об ошибке
        await callback.message.edit_text(
            "Извините, информация по этому вопросу временно недоступна.",
            reply_markup=get_question_keyboard()
        )


async def back_to_menu(callback: CallbackQuery, state: FSMContext) -> None:
    """
    Обработчик возврата в главное меню
    """
    await callback.answer()
    await callback.message.edit_text(
        "Выберите интересующий вас раздел:",
        reply_markup=get_menu_keyboard()
    )
    await state.set_state(UserState.menu)


def register_questions_handlers(router: Router) -> None:
    """
    Регистрирует обработчики для FAQ вопросов
    """
    # Регистрируем обработчики для каждого вопроса
    router.callback_query.register(process_faq_question, F.data.startswith("faq_"))
    
    # Регистрируем обработчик для возврата в меню
    router.callback_query.register(back_to_menu, F.data == "back_to_menu") 