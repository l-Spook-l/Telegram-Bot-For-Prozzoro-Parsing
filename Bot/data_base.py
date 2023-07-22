import sqlite3 as sq
from config import bot


# созадаем или подключаемся к БД
def sql_start():
    global base, cur
    # создаем подключение к БД
    base = sq.connect('prozorro_user_set.db')
    cur = base.cursor()  # для работы с БД
    if base:
        print('Data base connected OK!')

    # создаем таблицу если ее нету в бд
    base.execute(
        'CREATE TABLE IF NOT EXISTS user_settings('
        'id INTEGER PRIMARY KEY AUTOINCREMENT, '
        'User INTEGER , '
        'DK021_2015 TEXT, '
        'Status TEXT, '
        'Procurement_type TEXT, '
        'Region TEXT,'
        'Dispatch_time TEXT,'
        'Email TEXT)'
    )
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        print(tuple(data.values()))
        # подставляем значения
        cur.execute(
            'INSERT INTO user_settings (user, DK021_2015, Status, Procurement_type, Region, Dispatch_time, Email) VALUES (?, ?, ?, ?, ?, ?, ?)',
            tuple(data.values()))
        base.commit()
