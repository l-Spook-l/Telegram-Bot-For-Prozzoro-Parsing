import sqlite3 as sq



async def sql_read(message):
    print('databse2: ', message)
    list_test = []

    # перебираем все данные по таблицам в виде списка
    for ret in cur.execute(f'SELECT * FROM user_settings WHERE user == {message.from_user.id}').fetchall():
        print('ret', ret)
        # разбираем таблицу по столбцам
        list_test += f'ДК021:2015: {ret[2]}\nСтатус: {ret[3]}\nВид закупівлі: {ret[4]}\nРегіон: {ret[5]}\nЧас відправки: {ret[6]}\nПошта: {ret[7]}'
