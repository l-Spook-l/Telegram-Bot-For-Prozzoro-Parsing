import sqlite3 as sq
from config import bot


# созадем или подключаемся к БД
def sql_start():
    global base, cur
    # создаем подключение к БД
    base = sq.connect('prozorro_user_set.db')
    cur = base.cursor()  # для работы с БД
    if base:
        # если все норм
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
