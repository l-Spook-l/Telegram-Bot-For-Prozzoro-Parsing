from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Param = KeyboardButton('Ваші запити')
Add = KeyboardButton('Додати запит')
Delete = KeyboardButton('Видалити запит')

Skip = KeyboardButton('Пропустити')
Stop = KeyboardButton('Відміна')

markup = ReplyKeyboardMarkup(resize_keyboard=True)
markup_set = ReplyKeyboardMarkup(resize_keyboard=True)

markup.row(Param)
markup.row(Add, Delete)
markup_set.row(Skip, Stop)
