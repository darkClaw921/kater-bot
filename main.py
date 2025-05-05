import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties

from config import BOT_TOKEN
from handlers.start import register_start_handlers
from handlers.user_info import register_user_info_handlers
from handlers.menu import register_menu_handlers
from handlers.questions import register_questions_handlers

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


async def main():
    """Точка входа в программу"""
    # Проверка наличия токена
    if not BOT_TOKEN:
        logger.error("Токен бота не найден. Убедитесь, что переменная BOT_TOKEN задана в .env файле")
        return
    
    # Инициализация бота и диспетчера
    bot = Bot(token=BOT_TOKEN,default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=MemoryStorage())
    
    # Регистрация обработчиков
    register_start_handlers(dp)
    register_user_info_handlers(dp)
    register_menu_handlers(dp)
    register_questions_handlers(dp)
    
    # Запуск бота
    logger.info("Запуск бота WAKE.iv")
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Бот остановлен!")
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}", exc_info=True)
