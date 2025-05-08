from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto
import os

from data.faq import FAQ
from keyboards.menu_kb import get_menu_keyboard
from keyboards.question_kb import get_question_keyboard
from utils.states import UserState
from utils.photo import get_photo_path, get_photo_paths

router = Router()


async def process_faq_question(callback: CallbackQuery) -> None:
    """
    Общий обработчик для всех FAQ вопросов
    """
    await callback.answer()
    
    # Получаем ключ вопроса из callback_data (обрезаем префикс "faq_")
    faq_key = callback.data.replace("faq_", "")
    
    if faq_key in FAQ:
        faq_item = FAQ[faq_key]
        # Формируем ответ из вопроса и ответа
        response = f"<b>{faq_item['question']}</b>\n\n{faq_item['answer']}"
        
        # Проверяем, является ли это вопросом о мифах, который требует специальной обработки
        if faq_key == "myths" and faq_item.get("has_photo", False) and "photo_key" in faq_item:
            # Получаем все пути к фотографиям мифов
            photo_paths = get_photo_paths(faq_item["photo_key"])
            # Фильтруем только существующие файлы
            existing_paths = [path for path in photo_paths if os.path.exists(path)]
            
            if existing_paths:
                # Создаем медиа-группу для всех фотографий
                media_group = []
                # Первое фото с текстом
                media_group.append(InputMediaPhoto(
                    media=FSInputFile(existing_paths[0]),
                    caption=response
                ))
                
                # Добавляем остальные фото без текста
                for path in existing_paths[1:]:
                    media_group.append(InputMediaPhoto(media=FSInputFile(path)))
                
                # Удаляем предыдущее сообщение и отправляем медиа-группу
                await callback.message.delete()
                await callback.message.answer_media_group(media=media_group)
                
                # Отправляем клавиатуру отдельным сообщением, так как media_group не поддерживает reply_markup
                await callback.message.answer(
                    "Выберите другой вопрос или вернитесь в меню:",
                    reply_markup=get_question_keyboard()
                )
                return
        
        # Для всех остальных вопросов - стандартное поведение
        elif faq_item.get("has_photo", False) and "photo_key" in faq_item:
            photo_path = get_photo_path(faq_item["photo_key"])
            
            if photo_path and os.path.exists(photo_path):
                # Отправляем фото с ответом
                photo = FSInputFile(photo_path)
                await callback.message.delete()
                await callback.message.answer_photo(
                    photo=photo,
                    caption=response,
                    reply_markup=get_question_keyboard()
                )
                return
        
        # Отправляем только текстовый ответ и клавиатуру с вопросами
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