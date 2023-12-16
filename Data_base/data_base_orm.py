import sqlite3 as sq
from config import bot

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Создаем подключение к базе данных
Base = declarative_base()


# Определяем модель данных
class UserSettings(Base):
    __tablename__ = 'user_settings'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user = Column(Integer)
    DK021_2015 = Column(String)
    Status = Column(String)
    Procurement_type = Column(String)
    Region = Column(String)
    Dispatch_time = Column(String)
    Email = Column(String)


# Функция для создания сессии с базой данных
def create_session():
    db_file = 'prozorro_user_set.db'
    engine = create_engine(f'sqlite:///{db_file}')
    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    return Session(), not os.path.exists(db_file)


# Определяем сессию и проверяем наличие базы данных
session, db_created = create_session()


async def sql_add_data(state):
    print('orm work')
    try:
        async with state.proxy() as data:
            new_data = UserSettings(
                user=data['user'],
                DK021_2015=data['DK021_2015'],
                Status=data['Status'],
                Procurement_type=data['Procurement_type'],
                Region=data['Region'],
                Dispatch_time=data['Dispatch_time'],
                Email=data['Email']
            )
            session.add(new_data)
            session.commit()
            return True
    except Exception as error:
        print(f"Error occurred while adding data: {error}")
        session.rollback()
        return False


async def connect_db():
    if db_created:
        # Здесь вы можете выполнить необходимые действия при создании базы данных
        print('Bot online. Database created.')
    else:
        print('Bot online.')

# def sql_connect():
#     global base, cur
#     try:
#         with sq.connect('prozorro_user_set.db') as base:
#             cur = base.cursor()  # для работы с БД
#             print('Data base connected OK!')
#
#             # We create a table if it doesn't exist in the database.
#             cur.execute(
#                 'CREATE TABLE IF NOT EXISTS user_settings('
#                 'id INTEGER PRIMARY KEY AUTOINCREMENT, '
#                 'User INTEGER , '
#                 'DK021_2015 TEXT, '
#                 'Status TEXT, '
#                 'Procurement_type TEXT, '
#                 'Region TEXT,'
#                 'Dispatch_time TEXT,'
#                 'Email TEXT)'
#             )
#             base.commit()
#     except Exception as error:
#         print("Connection refused...")
#         print(f"Error - {error}")
#
#
# async def sql_add_data(state):
#     try:
#         async with state.proxy() as data:
#             cur.execute(
#                 'INSERT INTO user_settings (user, DK021_2015, Status, Procurement_type, Region, Dispatch_time, Email) '
#                 'VALUES (?, ?, ?, ?, ?, ?, ?)', tuple(data.values()))
#             base.commit()
#             return True
#     except sq.Error as error:
#         print(f"Error occurred while adding data: {error}")
#         return False
#
#
# async def sql_read(message):
#     try:
#         for ret in cur.execute(f'SELECT * FROM user_settings WHERE user = {message.from_user.id}').fetchall():
#             await bot.send_message(message.from_user.id,
#                                    f'ДК021:2015: {ret[2]}\nСтатус: {ret[3]}\nВид закупівлі: {ret[4]}\nРегіон: {ret[5]}\nЧас відправки: {ret[6]}\nПошта: {ret[7]}')
#         return True
#     except sq.Error as error:
#         print(f"Error occurred while reading data: {error}")
#         return False
#
#
# async def sql_read_for_del(message):
#     try:
#         return cur.execute(f'SELECT * FROM user_settings WHERE user = {message.from_user.id}').fetchall()
#     except sq.Error as error:
#         print(f"Error occurred while reading data: {error}")
#         return False
#
#
# async def sql_delete_data(data):
#     try:
#         cur.execute('DELETE FROM user_settings WHERE id = ?', (data,))
#         base.commit()
#         return True
#     except sq.Error as error:
#         print(f"Error occurred while remove data: {error}")
#         return False
#
#
# async def sql_read_time(time_now):
#     try:
#         return cur.execute('SELECT * FROM user_settings WHERE Dispatch_time = ?', (time_now,)).fetchall()
#     except sq.Error as error:
#         print(f"Error occurred while check time: {error}")
#
#
# async def sql_get_data(user_id, time):
#     data_list = []
#
#     try:
#         for ret in cur.execute(f'SELECT * FROM user_settings WHERE user = {user_id} AND Dispatch_time = ?',
#                                (time,)).fetchall():
#             data_list.append({
#                 'id': ret[0],
#                 'user': ret[1],
#                 'ДК021:2015': ret[2],
#                 'Статус': ret[3],
#                 'Вид закупівлі': ret[4],
#                 'Регіон': ret[5],
#                 'Час відправки': ret[6],
#                 'Пошта': ret[7],
#             })
#         return data_list
#     except sq.Error as error:
#         print(f"Error occurred while get data: {error}")
#         return False
