from aiogram import executor
import asyncio
import datetime
from config import dp
from Telegram_bot import client
from Data_base.data_base import sql_connect, sql_read_time, sql_get_data
from Parser.Email_connect import send_email


async def check_update_database():
    print('Start check update database')
    time_correction = datetime.timedelta(seconds=0)
    while True:
        await asyncio.sleep(60 - time_correction.total_seconds())
        now = datetime.datetime.now()
        formatted_time = now.strftime("%H:%M")
        print('=================Time now: ', datetime.datetime.now(), '===================================')
        check_data = await sql_read_time(formatted_time)
        # If there's something during the time check
        if check_data:
            data = await sql_get_data(check_data[0][1], formatted_time)
            if data:
                await send_email(data)
            else:
                print('Помилка з отриманням даних')
        time_correction = datetime.datetime.now() - now
        print(f'###################### Uncertainty - {time_correction.total_seconds()} ###############################')


async def on_startup(_):
    sql_connect()
    print('Bot online!')


client.register_handlers_client(dp)

if __name__ == "__main__":
    asyncio.ensure_future(check_update_database())
    executor.start_polling(dp, on_startup=on_startup)
