import os
from dotenv import load_dotenv

# Загрузка переменных окружения из .env файла
load_dotenv()

# Получение токена бота из переменных окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Настройки бота
BOT_NAME = "СёрфБро"
COMPANY_NAME = "WAKE.iv от компании NA BOARD" 