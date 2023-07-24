# файл точка входа
from aiogram import executor
from config import dp
from data_base import sql_start, sql_read_time
import client
import asyncio
import aioschedule as schedule  # для запуска в определенное время
import datetime


# Функция для запуска задачи по расписанию
async def check_update_database():
    schedule.every(1).minutes.do(sql_read_time)
    print('222')
    while True:
        await schedule.run_pending()
        await asyncio.sleep(10)
        print('111')
        print('Time now: ', datetime.datetime.now())




async def on_startup(_):
    sql_start()  # запускаем фун-ю подключаем БД
    print('Бот вышел в онлайн')


client.register_handlers_client(dp)

if __name__ == "__main__":
    # Запускаем асинхронный цикл с запуском задачи по расписанию
    asyncio.ensure_future(check_update_database())

    executor.start_polling(dp, on_startup=on_startup)
