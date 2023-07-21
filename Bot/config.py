# этот файл помогает обойти ошибку двойного импорта
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage  # помогает хранить данные в опре. памяти
import os

storage = MemoryStorage()  # для хранения данных в опер. памяти

# фильтр матов в 3ем видео
# подключаем токен бота
bot = Bot(token=os.getenv('TOKEN'))
# отслеживание событий
dp = Dispatcher(bot, storage=storage)
