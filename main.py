# файл точка входа
from aiogram import executor
import asyncio
# import aioschedule as schedule  # для запуска в определенное время
import datetime
from config import dp
from Telegram_bot import client
from Data_base.data_base import sql_start, sql_read_time, sql_get_data
from Parser.Email_connect import send_email


async def check_update_database():
    # schedule.every(1).minutes.do(sql_read_time)
    print('start check_update_database')
    while True:
        # await schedule.run_pending()
        await asyncio.sleep(20)
        now = datetime.datetime.now()
        formatted_time = now.strftime("%H:%M")
        user = await sql_read_time(formatted_time)

        if user:
            print('user', user)
            data = await sql_get_data(user[0][1], formatted_time)
            print('что-то есть', len(data))
            print('===========================================================')
            print('data', data)
            send_email(data)
            print('===========================================================')
        else:
            print('===========================================================')
            print('Time now: ', datetime.datetime.now())
            print('Ниче нет')
            print('===========================================================')


async def on_startup(_):
    sql_start()  # подключаем БД
    print('Бот вышел в онлайн')


client.register_handlers_client(dp)

if __name__ == "__main__":
    # Запускаем асинхронный цикл с запуском задачи по расписанию
    asyncio.ensure_future(check_update_database())
    executor.start_polling(dp, on_startup=on_startup)
