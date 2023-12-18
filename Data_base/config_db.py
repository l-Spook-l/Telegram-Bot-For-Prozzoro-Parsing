from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv
import os

load_dotenv()  # загрузка переменных окружения из файла .env в переменные окружения программы

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


class Base(DeclarativeBase):
    pass


# создаем движок
async_engine = create_async_engine(
    url=DATABASE_URL,  # путь к бд
    echo=False,  # у консоли все будет видно
    # pool_size=5, # макс одновременный подключений
    # max_overflow=10
)

# Создаем таблицы (если их нет)
async_session = async_sessionmaker(async_engine, expire_on_commit=False)
