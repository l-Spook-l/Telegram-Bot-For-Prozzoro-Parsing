from sqlalchemy import insert, select, delete
from .models import UserSettings
from .config_db import async_session


async def sql_add_data(state):
    try:
        async with async_session() as session:
            async with state.proxy() as data:
                stat = insert(UserSettings).values(**data)
                await session.execute(stat)
                await session.commit()
            return True
    except Exception as error:
        print(f"Error occurred while adding data: {error}")
        return False


async def sql_read(message):
    try:
        async with async_session() as session:
            query = select(UserSettings).filter_by(user=message.from_user.id)
            res = await session.execute(query)
            result = res.all()
        return result
    except Exception as error:
        print(f"Error occurred while reading data: {error}")
        return False


async def sql_read_for_del(message):
    try:
        async with async_session() as session:
            query = select(UserSettings).filter_by(user=message.from_user.id)
            res = await session.execute(query)
            result = res.all()
        return result
    except Exception as error:
        print(f"Error occurred while reading data: {error}")
        return False


async def sql_delete_data(id):
    try:
        async with async_session() as session:
            query = delete(UserSettings).filter_by(id=id)
            await session.execute(query)
            await session.commit()
        return True
    except Exception as error:
        print(f"Error occurred while remove data: {error}")
        return False


async def sql_read_time(time_now):
    try:
        async with async_session() as session:
            query = select(UserSettings).filter_by(Dispatch_time=time_now)
            res = await session.execute(query)
            result = res.all()
        return result
    except Exception as error:
        print(f"Error occurred while check time: {error}")


async def get_data_tender(data):
    data_list = []
    try:
        for user_tender in data:
            tender = user_tender[0]
            data_list.append({
                'id': tender.id,
                'user': tender.user,
                'ДК021:2015': tender.DK021_2015,
                'Статус': tender.Status,
                'Вид закупівлі': tender.Procurement_type,
                'Регіон': tender.Region,
                'Час відправки': tender.Dispatch_time,
                'Пошта': tender.Email,
            })
        return data_list
    except Exception as error:
        print(f"Error occurred while get data: {error}")
        return False
