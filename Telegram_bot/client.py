from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Data_base.data_base import sql_add_data, sql_read, sql_delete_data, sql_read_for_del
from config import bot
from .client_buttons import action_menu_markup, skip_cancel_markup
import re

dp = Dispatcher(bot)


# класс для состояний
class FSMClient(StatesGroup):
    DK021_2015 = State()
    Status = State()
    Procurement_type = State()
    Region = State()
    Dispatch_time = State()
    Email = State()


async def start_bot(message: types.Message):
    print('data about user', message)
    await message.answer("Вітаю, оберіть, що потрібно зробити", reply_markup=action_menu_markup)


async def create_new_request(message: types.Message):
    await FSMClient.DK021_2015.set()  # для ожидания ввода
    await message.answer('Введіть код ДК021:2015', reply_markup=skip_cancel_markup)


# выход из состояний (команда для отмены)
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Додавання нового запиту скасовано', reply_markup=action_menu_markup)


async def DK021_2015(message: types.Message, state: FSMContext):
    async with state.proxy() as data:  # работа со словарем машины состояний
        data['user'] = message.from_user.id
        data['DK021_2015'] = message.text.lower()
    await FSMClient.next()  # для ожидания ввода
    await message.answer('Введіть статус')


async def status(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Status'] = message.text.lower()
    await FSMClient.next()
    await message.answer('Введіть вид закупівлі')


async def procurement_type(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Procurement_type'] = message.text.lower()
    await FSMClient.next()
    await message.answer('Оберіть потрібний регіон')


async def region(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Region'] = message.text.lower()
    await FSMClient.next()
    await message.answer('Введіть час отправлення повідомлення на електронну пошту')


async def dispatch_time(message: types.Message, state: FSMContext):
    async with state.proxy() as data:  # работа со словарем машины состояний
        # Удаление всех символов кроме цифр
        cleaned_time = re.sub(r'\D', '', message.text)
        # Добавление символа ":" после первых двух цифр
        formatted_time = cleaned_time[:2] + ":" + cleaned_time[2:]
        data['Dispatch_time'] = formatted_time
    await FSMClient.next()
    await message.answer('Введіть адрес електронної пошти')


async def email(message: types.Message, state: FSMContext):
    async with state.proxy() as data:  # работа со словарем машины состояний
        data['Email'] = message.text.lower()
    success = await sql_add_data(state)  # записываем данные в бд
    if success:
        await message.answer('Новий запит успішно додано', reply_markup=action_menu_markup)
    else:
        await message.answer('Виникла внутрішня помилка, будь ласка спробуйте пізніше', reply_markup=action_menu_markup)
    await state.finish()  # тут заканчивается машина состояний


async def list_requests(message: types.Message):
    await message.reply('Список ваших запитів')
    # await sql_read(message)
    success = await sql_read(message)
    if not success:
        await message.answer('Виникла внутрішня помилка, будь ласка спробуйте пізніше', reply_markup=action_menu_markup)


# если событие - (del)
async def del_callback_run(callback_query: types.CallbackQuery):
    # удаляем выбраную запись
    # await sql_delete_data(callback_query.data.replace('del ', ''))
    success = await sql_delete_data(callback_query.data.replace('del ', ''))
    if success:
        # и отвечаем для окончания процесса
        await callback_query.answer(text='Запит успішно видалено', show_alert=True)
    else:
        await callback_query.answer(text='Виникла внутрішня помилка, будь ласка спробуйте пізніше', show_alert=True)


# добавляем кнопку удалить
async def delete_item(message: types.Message):
    # читаем данные из бд
    read = await sql_read_for_del(message)
    if read:
        for ret in read:
            # отправляем данные и создаем кнопки для каждого запроса
            await bot.send_message(message.from_user.id,
                                   f'ДК021:2015: {ret[2]}\nСтатус: {ret[3]}\nВид закупівлі: {ret[4]}\nРегіон: {ret[5]}\nЧас відправки: {ret[6]}\nПошта: {ret[7]}',
                                   reply_markup=InlineKeyboardMarkup().add(
                                       InlineKeyboardButton('Видалити', callback_data=f'del {ret[0]}')))
    else:
        await message.answer('Виникла внутрішня помилка, будь ласка спробуйте пізніше', reply_markup=action_menu_markup)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_bot, commands=['start', 'help'], state=None)

    dp.register_message_handler(create_new_request, commands=['Додати запит'], state=None)
    dp.register_message_handler(create_new_request, Text(equals='Додати запит', ignore_case=True),
                                state=None)

    dp.register_message_handler(cancel_handler, state="*", commands='Відміна')
    dp.register_message_handler(cancel_handler, Text(equals='Відміна', ignore_case=True), state="*")

    dp.register_message_handler(DK021_2015, state=FSMClient.DK021_2015)
    dp.register_message_handler(status, state=FSMClient.Status)
    dp.register_message_handler(procurement_type, state=FSMClient.Procurement_type)
    dp.register_message_handler(region, state=FSMClient.Region)
    dp.register_message_handler(dispatch_time, state=FSMClient.Dispatch_time)
    dp.register_message_handler(email, state=FSMClient.Email)

    dp.register_message_handler(list_requests, Text(equals='Ваші запити', ignore_case=True))

    dp.register_callback_query_handler(del_callback_run, lambda x: x.data and x.data.startswith('del '))
    dp.register_message_handler(delete_item, commands='Видалити запит')
    dp.register_message_handler(delete_item, Text(equals='Видалити запит', ignore_case=True))
