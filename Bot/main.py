# файл точка входа
from aiogram import executor
from config import dp
from data_base import sql_start


async def on_startup(_):
    sql_start()  # запускаем фун-ю подключаем БД
    print('Бот вышел в онлайн')


executor.start_polling(dp, on_startup=on_startup)
