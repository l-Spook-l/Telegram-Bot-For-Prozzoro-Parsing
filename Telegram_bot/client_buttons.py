from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Param = KeyboardButton('Ваші запити')
Add = KeyboardButton('Додати запит')
Delete = KeyboardButton('Видалити запит')

Skip = KeyboardButton('Пропустити')
Stop = KeyboardButton('Відміна')

action_menu_markup = ReplyKeyboardMarkup(resize_keyboard=True)
skip_cancel_markup = ReplyKeyboardMarkup(resize_keyboard=True)

action_menu_markup.row(Param)
action_menu_markup.row(Add, Delete)
skip_cancel_markup.row(Skip, Stop)
