# инлайн кнопки
from aiogram import Bot, Dispatcher, executor, types
from client_buttons import markup
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext  # для аннотации типов
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from data_base import sql_add_command, sql_read, sql_delete_command, sql_read_for_del
from config import bot

# подключаем токен бота
# bot = Telegram_bot('5310179992:AAEXZajyqsQzHD8')
# отслеживание событий
dp = Dispatcher(bot)

ID = None


# класс для состояний
class FSMClient(StatesGroup):
    DK021_2015 = State()
    Status = State()
    Procurement_type = State()
    Region = State()
    Dispatch_time = State()
    Email = State()


# @dp.message_handler(commands=['start'], state=None)
async def commands_start(message: types.Message):
    global ID
    ID = message.from_user.id
    if message.from_user.id != 619709171:
        await message.answer("Вітаю оберіть, що потрібно зробити", reply_markup=markup)
    print(message.from_user.id)
    # Замовник    # Учасник    # Закупівельник    # ДК021:2015
    # Статус    # Вид закупівлі    # Регіон    # Очікувана вартість
    # Дати    # Обґрунтування    # Оцінка пропозицій    # Умови оплати


# @dp.message_handler(commands=['Обновить'])
async def update(message: types.Message):
    if message.from_user.id == ID:  # если id админа
        await FSMClient.DK021_2015.set()  # для ожидания ввода
        await message.reply('Введіть код ДК021:2015')


# выход из состояний (команда для отмены)
# @dp.register_message_handler(state="*", commands='отмена')  # для команды
# @dp.register_message_handler(Text(equals='отмена', ignore_case=True), state="*")  # для обычного текста
async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('Додавання нового запиту скасовано')


# @dp.message_handler(state=FSMClient.DK021_2015)
async def DK021_2015(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:  # работа со словарем машины состояний
            # сохраняем в словарь машины состояния
            data['user'] = ID
            data['DK021_2015'] = message.text
        await FSMClient.next()  # для ожидания ввода
        await message.answer('Введіть статус')


# @dp.message_handler(state=FSMClient.Status)
async def status(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:  # работа со словарем машины состояний
            # сохраняем в словарь машины состояния
            data['Status'] = message.text
        await FSMClient.next()  # для ожидания ввода
        await message.answer('Введіть вид закупівлі')


# @dp.message_handler(state=FSMClient.Procurement_type)
async def procurement_type(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:  # работа со словарем машины состояний
            # сохраняем в словарь машины состояния
            data['Procurement_type'] = message.text
        await FSMClient.next()  # для ожидания ввода
        await message.answer('Оберіть потрібний регіон')


# @dp.message_handler(state=FSMClient.Region)
async def region(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:  # работа со словарем машины состояний
            # сохраняем в словарь машины состояния
            data['Region'] = message.text
        await FSMClient.next()  # для ожидания ввода
        await message.answer('Введіть час отправлення повідомлення на електронну пошту')


async def dispatch_time(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:  # работа со словарем машины состояний
            # сохраняем в словарь машины состояния
            data['Dispatch_time'] = message.text
        await FSMClient.next()  # для ожидания ввода
        await message.answer('Введіть адрес електронної пошти')


async def email(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:  # работа со словарем машины состояний
            # сохраняем в словарь машины состояния
            data['Email'] = message.text
        # тут надо бы все записать в БД
        await sql_add_command(state)  # записываем данные в бд
        await message.answer('Новий запит успішно додано')
        await state.finish()  # тут заканчивается машина состояний


async def param(message: types.Message):
    await message.reply('Список ваших запитів')
    await sql_read(message)


# если событие - (del )
# @dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run(callback_query: types.CallbackQuery):
    # удаляем выбраную запись
    await sql_delete_command(callback_query.data.replace('del ', ''))
    # и отвечам для окончания процесса
    # show_alert - всплывающие окно
    # await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} удалена.', show_alert=True)
    await callback_query.answer(text='Запит успішно видалено', show_alert=True)


# добавляем кнопку удалить
# @dp.message_handler(commands='Видалити запит')
async def delete_item(message: types.Message):
    if message.from_user.id == ID:  # проверка
        # читаем из бд все
        print('message', message)
        read = await sql_read_for_del(message)  # читаем данные из бд
        print('read', read)
        for ret in read:
            print('ret', ret)
            # отправляем  данные и создаем кнопки для каждого запроса
            await bot.send_message(message.from_user.id,
                                   f'ДК021:2015: {ret[2]}\nСтатус: {ret[3]}\nВид закупівлі: {ret[4]}\nРегіон: {ret[5]}\nЧас відправки: {ret[6]}\nПошта: {ret[7]}',
                                   reply_markup=InlineKeyboardMarkup().add(
                                       InlineKeyboardButton('Видалити', callback_data=f'del {ret[0]}')))


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'], state=None)

    dp.register_message_handler(update, commands=['Додати запит'], state=None)
    dp.register_message_handler(update, Text(equals='Додати запит', ignore_case=True), state=None)  # обычный текста

    dp.register_message_handler(cancel_handler, state="*", commands='Відміна')  # для команды для любого - state="*"
    dp.register_message_handler(cancel_handler, Text(equals='Відміна', ignore_case=True), state="*")  # обычный текста

    dp.register_message_handler(DK021_2015, state=FSMClient.DK021_2015)
    dp.register_message_handler(status, state=FSMClient.Status)
    dp.register_message_handler(procurement_type, state=FSMClient.Procurement_type)
    dp.register_message_handler(region, state=FSMClient.Region)
    dp.register_message_handler(dispatch_time, state=FSMClient.Dispatch_time)
    dp.register_message_handler(email, state=FSMClient.Email)

    dp.register_message_handler(param, Text(equals='Ваші запити', ignore_case=True))  # обычный текста

    dp.register_callback_query_handler(del_callback_run, lambda x: x.data and x.data.startswith('del '))
    dp.register_message_handler(delete_item, commands='Видалити запит')
    dp.register_message_handler(delete_item, Text(equals='Видалити запит', ignore_case=True))
