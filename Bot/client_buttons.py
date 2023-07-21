from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Param = KeyboardButton('Ваші запити')
Add = KeyboardButton('Додати запит')
Update = KeyboardButton('Редагувати запит')
Delete = KeyboardButton('Видалити запит')
Stop = KeyboardButton('Відміна')

markup = ReplyKeyboardMarkup(resize_keyboard=True)

markup.row(Param)
markup.row(Add, Update, Delete)
markup.row(Stop)
