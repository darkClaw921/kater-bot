import os
from dotenv import load_dotenv

# Загрузка переменных окружения из .env файла
load_dotenv()

# Получение токена бота из переменных окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Настройки бота
BOT_NAME = "СёрфБро"
COMPANY_NAME = "WAKE.iv от клуба NA BOARD"

# Информация о графике работы
WORK_HOURS = {
    "weekdays": "11:00 до 20:00",
    "weekend": "10:00 до 20:00"
} 