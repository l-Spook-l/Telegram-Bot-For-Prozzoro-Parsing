from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os
from dotenv import load_dotenv
load_dotenv()

# для хранения данных в опер. памяти
storage = MemoryStorage()

# подключаем токен бота
bot = Bot(token=os.getenv('TOKEN'))
# отслеживание событий
dp = Dispatcher(bot, storage=storage)
