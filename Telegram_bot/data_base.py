import sqlite3 as sq
from config import bot


# созадаем или подключаемся к БД
def sql_start():
    print('eqewqewqeqew')
    global base, cur
    # создаем подключение к БД
    base = sq.connect('../prozorro_user_set.db')
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


async def sql_read(message):
    print('databse2: ', message)
    # перебираем все данные по таблицам в виде списка
    for ret in cur.execute(f'SELECT * FROM user_settings WHERE user == {message.from_user.id}').fetchall():
        print('ret', ret)
        # разбираем таблицу по столбцам
        await bot.send_message(message.from_user.id,
                               f'ДК021:2015: {ret[2]}\nСтатус: {ret[3]}\nВид закупівлі: {ret[4]}\nРегіон: {ret[5]}\nЧас відправки: {ret[6]}\nПошта: {ret[7]}')


async def sql_read_for_del(message):
    print('user', message.from_user.id)
    return cur.execute(f'SELECT * FROM user_settings WHERE user == {message.from_user.id}').fetchall()


async def sql_delete_command(data):
    print('data', data)
    cur.execute('DELETE FROM user_settings WHERE id == ?', (data,))
    base.commit()


async def sql_read_time():
    res = cur.execute('SELECT id, Dispatch_time FROM user_settings').fetchall()
    print(res)
    return res
