import sqlite3 as sq


def connect_database():
    global base, cur
    base = sq.connect('../prozorro_user_set.db')
    cur = base.cursor()  # для работы с БД
    if base:
        print('Data base connected OK!')


def sql_read(message):
    print('databse2: ', message)
    list_test = []

    # перебираем все данные по таблицам в виде списка
    for ret in cur.execute(f'SELECT * FROM user_settings WHERE User == {message}').fetchall():
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
