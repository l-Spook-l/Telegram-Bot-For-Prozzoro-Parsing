import sqlite3 as sq
from config import bot


# создаем или подключаемся к БД
def sql_connect():
    global base, cur
    try:
        # создаем подключение к БД
        with sq.connect('prozorro_user_set.db') as base:
            cur = base.cursor()  # для работы с БД
            print('Data base connected OK!')

            # создаем таблицу если ее нету в бд
            cur.execute(
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
        # # создаем подключение к БД
        # base = sq.connect('prozorro_user_set.db')
        # cur = base.cursor()  # для работы с БД
        # if base:
        #     print('Data base connected OK!')
        #
        # # создаем таблицу если ее нету в бд
        # base.execute(
        #     'CREATE TABLE IF NOT EXISTS user_settings('
        #     'id INTEGER PRIMARY KEY AUTOINCREMENT, '
        #     'User INTEGER , '
        #     'DK021_2015 TEXT, '
        #     'Status TEXT, '
        #     'Procurement_type TEXT, '
        #     'Region TEXT,'
        #     'Dispatch_time TEXT,'
        #     'Email TEXT)'
        # )
        # base.commit()
    except Exception as error:
        print("Connection refused...")
        print(f"Error - {error}")


async def sql_add_data(state):
    try:
        async with state.proxy() as data:
            cur.execute(
                'INSERT INTO user_settings (user, DK021_2015, Status, Procurement_type, Region, Dispatch_time, Email) '
                'VALUES (?, ?, ?, ?, ?, ?, ?)', tuple(data.values()))
            base.commit()
            return True
    except sq.Error as error:
        print(f"Error occurred while adding data: {error}")
        return False


async def sql_read(message):
    try:
        # проходимся по всем запросам пользователя
        for ret in cur.execute(f'SELECT * FROM user_settings WHERE user = {message.from_user.id}').fetchall():
            # возвращаем все запросы, для нужного пользователя
            await bot.send_message(message.from_user.id,
                                   f'ДК021:2015: {ret[2]}\nСтатус: {ret[3]}\nВид закупівлі: {ret[4]}\nРегіон: {ret[5]}\nЧас відправки: {ret[6]}\nПошта: {ret[7]}')
        return True
    except sq.Error as error:
        print(f"Error occurred while reading data: {error}")
        return False


async def sql_read_for_del(message):
    # получаем список запросов для удаления
    return cur.execute(f'SELECT * FROM user_settings WHERE user = {message.from_user.id}').fetchall()


async def sql_delete_data(data):
    # удаляем выбранный запрос
    cur.execute('DELETE FROM user_settings WHERE id = ?', (data,))
    base.commit()


async def sql_read_time(time_now):
    # мониторим время
    return cur.execute('SELECT * FROM user_settings WHERE Dispatch_time = ?', (time_now,)).fetchall()


async def sql_get_data(user_id, time):
    data_list = []

    # перебираем все данные по таблицам в виде списка
    for ret in cur.execute(f'SELECT * FROM user_settings WHERE User = {user_id} AND Dispatch_time = ?',
                           (time,)).fetchall():
        # разбираем таблицу по столбцам
        data_list.append({
            'id': ret[0],
            'user': ret[1],
            'ДК021:2015': ret[2],
            'Статус': ret[3],
            'Вид закупівлі': ret[4],
            'Регіон': ret[5],
            'Час відправки': ret[6],
            'Пошта': ret[7],
        })
    return data_list
