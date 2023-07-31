import sqlite3 as sq
from config import bot


# созадаем или подключаемся к БД
def sql_start():
    print('sql_start')
    global base, cur]
    try:
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
    except Exception as error:
        print("Connection refused...")
        print(f"Error - {error}")


async def sql_add_command(state):
    async with state.proxy() as data:
        # подставляем значения
        cur.execute(
            'INSERT INTO user_settings (user, DK021_2015, Status, Procurement_type, Region, Dispatch_time, Email) VALUES (?, ?, ?, ?, ?, ?, ?)',
            tuple(data.values()))
        base.commit()


async def sql_read(message):
    print('sql_read: ', message)
    # перебираем все данные по таблицам в виде списка
    for ret in cur.execute(f'SELECT * FROM user_settings WHERE user = {message.from_user.id}').fetchall():
        print('ret', ret)
        # разбираем таблицу по столбцам
        await bot.send_message(message.from_user.id,
                               f'ДК021:2015: {ret[2]}\nСтатус: {ret[3]}\nВид закупівлі: {ret[4]}\nРегіон: {ret[5]}\nЧас відправки: {ret[6]}\nПошта: {ret[7]}')


async def sql_read_for_del(message):
    print('user', message.from_user.id)
    return cur.execute(f'SELECT * FROM user_settings WHERE user = {message.from_user.id}').fetchall()


async def sql_delete_command(data):
    print('data', data)
    cur.execute('DELETE FROM user_settings WHERE id = ?', (data,))
    base.commit()


async def sql_read_time(time_now):
    res = cur.execute('SELECT * FROM user_settings WHERE Dispatch_time = ?', (time_now,)).fetchall()
    print('sql_read_time', res)
    return res


async def sql_get_data(user_id, time):
    print('sql_get_data: ', user_id)
    list_test = []

    # перебираем все данные по таблицам в виде списка
    for ret in cur.execute(f'SELECT * FROM user_settings WHERE User = {user_id} AND Dispatch_time = ?',
                           (time,)).fetchall():
        print('ret', ret)
        # разбираем таблицу по столбцам
        list_test.append({
            'id': ret[0],
            'user': ret[1],
            'ДК021:2015': ret[2],
            'Статус': ret[3],
            'Вид закупівлі': ret[4],
            'Регіон': ret[5],
            'Час відправки': ret[6],
            'Пошта': ret[7],
        })
    return list_test
