from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto
import os

from keyboards.question_kb import get_question_keyboard
from keyboards.menu_kb import get_menu_keyboard
from utils.states import UserState
from utils.photo import get_photo_path, get_photo_paths
from data.faq import WAKESURFING_INFO, WAKEBOARDING_INFO, PRICE_INFO, TEAM_INFO

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
    
    # Получаем пути к фотографиям вейксерфинга
    photo_paths = get_photo_paths("wakesurfing")
    
    # Проверяем наличие фотографий
    existing_paths = [path for path in photo_paths if os.path.exists(path)]
    
    # Если есть фото, отправляем их в виде альбома
    if existing_paths:
        # Создаем медиа-группу для всех фотографий
        media_group = []
        
        # Первое фото с ограниченной подписью (максимум 1024 символа)
        caption = WAKESURFING_INFO[:1024] if len(WAKESURFING_INFO) > 1024 else WAKESURFING_INFO
        
        # Добавляем первое фото с подписью
        media_group.append(InputMediaPhoto(
            media=FSInputFile(existing_paths[0]),
            caption=caption
        ))
        
        # Добавляем остальные фото без текста
        for path in existing_paths[1:]:
            media_group.append(InputMediaPhoto(media=FSInputFile(path)))
        
        # Удаляем предыдущее сообщение
        await callback.message.delete()
        
        # Отправляем альбом
        await callback.message.answer_media_group(media=media_group)
        
        # Если текст был слишком длинным, отправляем оставшуюся часть текста
        additional_text = ""
        if len(WAKESURFING_INFO) > 1024:
            additional_text = WAKESURFING_INFO[1024:]
        
        # Отправляем клавиатуру отдельным сообщением (с остатком текста, если есть)
        await callback.message.answer(
            additional_text + ("\n\nВыберите другой раздел:" if not additional_text else ""),
            reply_markup=get_menu_keyboard()
        )
    else:
        # Если нет фото, просто отправляем текст
        await callback.message.edit_text(
            WAKESURFING_INFO, 
            reply_markup=get_menu_keyboard()
        )


async def process_menu_wakeboarding(callback: CallbackQuery) -> None:
    """
    Обработчик выбора раздела 'Про вейкбординг'
    """
    await callback.answer()
    
    # Получаем пути к фотографиям вейкбординга
    photo_paths = get_photo_paths("wakeboarding")
    
    # Проверяем наличие фотографий
    existing_paths = [path for path in photo_paths if os.path.exists(path)]
    
    # Если есть фото, отправляем их в виде альбома
    if existing_paths:
        # Создаем медиа-группу для всех фотографий
        media_group = []
        
        # Первое фото с ограниченной подписью (максимум 1024 символа)
        caption = WAKEBOARDING_INFO[:1024] if len(WAKEBOARDING_INFO) > 1024 else WAKEBOARDING_INFO
        
        # Добавляем первое фото с подписью
        media_group.append(InputMediaPhoto(
            media=FSInputFile(existing_paths[0]),
            caption=caption
        ))
        
        # Добавляем остальные фото без текста
        for path in existing_paths[1:]:
            media_group.append(InputMediaPhoto(media=FSInputFile(path)))
        
        # Удаляем предыдущее сообщение
        await callback.message.delete()
        
        # Отправляем альбом
        await callback.message.answer_media_group(media=media_group)
        
        # Если текст был слишком длинным, отправляем оставшуюся часть текста
        additional_text = ""
        if len(WAKEBOARDING_INFO) > 1024:
            additional_text = WAKEBOARDING_INFO[1024:]
        
        # Отправляем клавиатуру отдельным сообщением (с остатком текста, если есть)
        await callback.message.answer(
            additional_text + ("\n\nВыберите другой раздел:" if not additional_text else ""),
            reply_markup=get_menu_keyboard()
        )
    else:
        # Если нет фото, просто отправляем текст
        await callback.message.edit_text(
            WAKEBOARDING_INFO,
            reply_markup=get_menu_keyboard()
        )


async def process_menu_price(callback: CallbackQuery) -> None:
    """
    Обработчик выбора раздела 'Прайс'
    """
    await callback.answer()
    await callback.message.edit_text(
        PRICE_INFO,
        reply_markup=get_menu_keyboard()
    )


async def process_menu_team(callback: CallbackQuery) -> None:
    """
    Обработчик выбора раздела 'Команда'
    """
    await callback.answer()
    await callback.message.edit_text(
        TEAM_INFO,
        reply_markup=get_menu_keyboard()
    )


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