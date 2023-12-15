from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Data_base.data_base import sql_add_data, sql_read, sql_delete_data, sql_read_for_del
from config import bot
from .client_buttons import action_menu_markup, skip_cancel_markup
from options import status_data, procurement_type_data, regions_data
import re

dp = Dispatcher(bot)


class FSMClient(StatesGroup):
    DK021_2015 = State()
    Status = State()
    Procurement_type = State()
    Region = State()
    Dispatch_time = State()
    Email = State()


async def start_bot(message: types.Message):
    await message.answer("Вітаю, оберіть, що потрібно зробити", reply_markup=action_menu_markup)


async def help_user(message: types.Message):
    await message.answer(
        "Інструкція використання бота."
        "\nУ нашому боті ви можете налаштувати параметри потрібних вам тендерів та отримувати їх на електронну пошту. "
        "\nНаразі реалізований пошук тендерів за чотирма параметрами: Статус, Вид закупівлі, ДК021:2015 та Регіон. "
        "\nДля параметру Регіон можна вказати лише одне значення у одному запиті (це обмеження Prozorro), "
        "а для решти параметрів можна вказувати кілька значень, розділивши їх комами."
        "\n                   Приклад запиту:"
        "\nДК021:2015: 09300000-2"
        "\nСтатус: період уточнень, прекваліфікація"
        "\nВид закупівлі: спрощена закупівля"
        "\nРегіон: київська область"
        "\nЧас відправки: 18:08"
        "\nПошта: ваша пошта"
        "\nТакож якщо вам щось не потрібно, ви можете натиснути кнопку - пропустити."
        "\nКонтакти: uaspookua@gmail.com",
        reply_markup=action_menu_markup)


@dp.message_handler(content_types=types.ContentType.TEXT)
async def create_new_request(message: types.Message):
    await FSMClient.DK021_2015.set()
    await message.answer('Введіть код ДК021:2015', reply_markup=skip_cancel_markup)


async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Додавання нового запиту скасовано', reply_markup=action_menu_markup)


@dp.message_handler(content_types=types.ContentType.TEXT)
async def DK021_2015(message: types.Message, state: FSMContext):
    # Pattern for checking the DK021_2015 code
    pattern = r'^\d{8}-\d{1,3}$'
    async with state.proxy() as data:
        DK021_2015_input = message.text.lower()
        if re.match(pattern, DK021_2015_input) or DK021_2015_input == 'пропустити':
            data['user'] = message.from_user.id
            data['DK021_2015'] = DK021_2015_input
            await FSMClient.next()
            await message.answer('Введіть статус')
        else:
            await message.answer('Не вірний код, спробуйте ще раз')
            await message.answer('Введіть код ДК021:2015')


@dp.message_handler(content_types=types.ContentType.TEXT)
async def status(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        status_input = message.text.lower().split(', ')

        valid_statuses = [status for status in status_input if status in status_data or status == 'пропустити']

        if valid_statuses:
            data['Status'] = ', '.join(valid_statuses)
            await FSMClient.next()
            await message.answer('Введіть вид закупівлі')
        else:
            await message.answer('Такого статусу немає, спробуйте ще раз')
            await message.answer('Введіть статус')


@dp.message_handler(content_types=types.ContentType.TEXT)
async def procurement_type(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        procurement_type_input = message.text.lower().split(', ')

        valid_procurement_types = [procurement_type for procurement_type in procurement_type_input if
                                   procurement_type in procurement_type_data or procurement_type == 'пропустити']
        if valid_procurement_types:
            data['Procurement_type'] = ', '.join(valid_procurement_types)
            await FSMClient.next()
            await message.answer('Оберіть потрібний регіон')
        else:
            await message.answer('Такого виду закупівлі немає, спробуйте ще раз')
            await message.answer('Введіть вид закупівлі')


@dp.message_handler(content_types=types.ContentType.TEXT)
async def region(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        region_input = message.text.lower().split(', ')
        valid_region = [region for region in region_input if region in regions_data or region == 'пропустити']
        if valid_region:
            data['Region'] = ', '.join(valid_region)
            await FSMClient.next()
            await message.answer('Введіть час отправлення повідомлення на електронну пошту')
        else:
            await message.answer('Такого регіону немає, спробуйте ще раз')
            await message.answer('Оберіть потрібний регіон')


@dp.message_handler(content_types=types.ContentType.TEXT)
async def dispatch_time(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        # Removing all characters except digits.
        cleaned_time = re.sub(r'\D', '', message.text)
        # Adding a colon ':' after the first two digits.
        formatted_time = cleaned_time[:2] + ":" + cleaned_time[2:]
        data['Dispatch_time'] = formatted_time
    await FSMClient.next()
    await message.answer('Введіть адрес електронної пошти')


@dp.message_handler(content_types=types.ContentType.TEXT)
async def email(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Email'] = message.text.lower()
    success = await sql_add_data(state)
    if success:
        await message.answer('Новий запит успішно додано', reply_markup=action_menu_markup)
    else:
        await message.answer('Виникла внутрішня помилка, будь ласка спробуйте пізніше', reply_markup=action_menu_markup)
    await state.finish()


async def list_requests(message: types.Message):
    await message.reply('Список ваших запитів')
    success = await sql_read(message)
    if not success:
        await message.answer('Виникла внутрішня помилка, будь ласка спробуйте пізніше', reply_markup=action_menu_markup)


async def del_callback_run(callback_query: types.CallbackQuery):
    success = await sql_delete_data(callback_query.data.replace('del ', ''))
    if success:
        await callback_query.answer(text='Запит успішно видалено', show_alert=True)
    else:
        await callback_query.answer(text='Виникла внутрішня помилка, будь ласка спробуйте пізніше', show_alert=True)


async def delete_item(message: types.Message):
    read = await sql_read_for_del(message)
    if read:
        for ret in read:
            await bot.send_message(message.from_user.id,
                                   f'ДК021:2015: {ret[2]}\nСтатус: {ret[3]}\nВид закупівлі: {ret[4]}\nРегіон: {ret[5]}\nЧас відправки: {ret[6]}\nПошта: {ret[7]}',
                                   reply_markup=InlineKeyboardMarkup().add(
                                       InlineKeyboardButton('Видалити', callback_data=f'del {ret[0]}')))
    else:
        await message.answer('Виникла внутрішня помилка, будь ласка спробуйте пізніше', reply_markup=action_menu_markup)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_bot, commands=['start'], state=None)

    dp.register_message_handler(help_user, commands=['help', 'Довідка'], state=None)
    dp.register_message_handler(help_user, Text(equals='Довідка', ignore_case=True), state=None)

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
