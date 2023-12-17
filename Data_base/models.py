from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Создаем подключение к базе данных
Base = declarative_base()


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
