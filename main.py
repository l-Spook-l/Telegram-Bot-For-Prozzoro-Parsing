# файл точка входа
from aiogram import executor
import asyncio
import aioschedule as schedule  # для запуска в определенное время
import datetime
from config import dp
from Telegram_bot import client
from Data_base.data_base import sql_start, sql_read_time, sql_read_time_2, sql_get_data
from Parser.Email_connect import send_email


# Функция для запуска задачи по расписанию
async def check_update_database():
    schedule.every(1).minutes.do(sql_read_time)
    # schedule.every(1).minutes.do(sql_read_time_2(12))
    print('start check_update_database')
    while True:
        now = datetime.datetime.now()
        formatted_time = now.strftime("%H")
        print("Formatted time:", formatted_time)
        print(type(int(formatted_time)))

        await schedule.run_pending()
        await asyncio.sleep(60)
        user = await sql_read_time_2(20)
        print('user', user)
        data = await sql_get_data(user[0][1], 20)
        if data:
            print('что-то есть', len(data))

        print('user', user[0][1])
        print('data', data)
        print('Time now: ', datetime.datetime.now())
        print('===========================================================')
        send_email(data)
        print('===========================================================')


async def on_startup(_):
    sql_start()  # запускаем фун-ю подключаем БД
    print('Бот вышел в онлайн')


client.register_handlers_client(dp)

if __name__ == "__main__":
    # Запускаем асинхронный цикл с запуском задачи по расписанию
    asyncio.ensure_future(check_update_database())
    executor.start_polling(dp, on_startup=on_startup)
