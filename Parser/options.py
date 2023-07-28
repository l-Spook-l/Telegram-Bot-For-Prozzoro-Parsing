# https://prozorro.gov.ua/api/search/tenders?filterType=tenders&sort_by=value.amount&order=desc&page=1
# &status%5B0%5D=active.enquiries
# &status%5B1%5D=active.tendering
# &status%5B2%5D=active.pre-qualification
# &status%5B3%5D=active.pre-qualification.stand-still
# &status%5B4%5D=active.auction
# &status%5B5%5D=active.qualification
# &status%5B6%5D=active.qualification.stand-still
# &status%5B7%5D=active.awarded
# &status%5B8%5D=unsuccessful
# &status%5B9%5D=cancelled
# &status%5B10%5D=complete
# &status%5B11%5D=active
# &status%5B12%5D=active.stage2.pending
# &status%5B13%5D=active.stage2.waiting


# https://prozorro.gov.ua/api/search/tenders?filterType=tenders
# &region=1-6
# &status%5B1%5D=active.tendering
# &status%5B11%5D=active
# &proc_type%5B1%5D=aboveThreshold
# &cpv%5B0%5D=71630000-3
# &cpv%5B1%5D=71630000-6
# &cpv%5B2%5D=50410000-2

status = {
    # 'Період уточнень': '&status%5B0%5D=active.enquiries',
    # 'Подання пропозицій': '&status%5B1%5D=active.tendering',
    # 'Прекваліфікація': '&status%5B2%5D=active.pre-qualification',
    # 'Прекваліфікація (період оскарження)': '&status%5B3%5D=active.pre-qualification.stand-still',
    # 'Аукціон': '&status%5B4%5D=active.auction',
    # 'Кваліфікація переможця': '&status%5B5%5D=active.qualification',
    # 'Кваліфікація переможця (період оскарження)': '&status%5B6%5D=active.qualification.stand-still',
    # 'Пропозиції розглянуті': '&status%5B7%5D=active.awarded',
    # 'Торги не відбулися': '&status%5B8%5D=unsuccessful',
    # 'Торги відмінено': '&status%5B9%5D=cancelled',
    # 'Завершена': '&status%5B10%5D=complete',
    # 'Підготовка угоди': '&status%5B11%5D=active',
    # 'Підготовка до 2-го етапу': '&status%5B12%5D=active.stage2.pending',
    # 'Створення 2-го етапу': '&status%5B13%5D=active.stage2.waiting',
    'Період уточнень': 'active.enquiries',
    'Подання пропозицій': 'active.tendering',
    'Прекваліфікація': 'active.pre-qualification',
    'Прекваліфікація (період оскарження)': 'active.pre-qualification.stand-still',
    'Аукціон': 'active.auction',
    'Кваліфікація переможця': 'active.qualification',
    'Кваліфікація переможця (період оскарження)': 'active.qualification.stand-still',
    'Пропозиції розглянуті': 'active.awarded',
    'Торги не відбулися': 'unsuccessful',
    'Торги відмінено': 'cancelled',
    'Завершена': 'complete',
    'Підготовка угоди': 'active',
    'Підготовка до 2-го етапу': 'active.stage2.pending',
    'Створення 2-го етапу': 'active.stage2.waiting',
}

# https://prozorro.gov.ua/api/search/tenders?filterType=tenders
# &proc_type%5B0%5D=belowThreshold
# &proc_type%5B1%5D=aboveThreshold
# &proc_type%5B2%5D=aboveThresholdUA
# &proc_type%5B3%5D=aboveThresholdEU
# &proc_type%5B4%5D=negotiation
# &proc_type%5B5%5D=negotiation.quick
# &proc_type%5B6%5D=aboveThresholdUA.defense
# &proc_type%5B7%5D=competitiveDialogueUA
# &proc_type%5B8%5D=competitiveDialogueEU
# &proc_type%5B9%5D=competitiveDialogueUA.stage2
# &proc_type%5B10%5D=competitiveDialogueEU.stage2
# &proc_type%5B11%5D=reporting
# &proc_type%5B12%5D=esco
# &proc_type%5B13%5D=closeFrameworkAgreementUA
# &proc_type%5B14%5D=closeFrameworkAgreementSelectionUA
# &proc_type%5B15%5D=priceQuotation
# &proc_type%5B16%5D=simple.defense

procurement_type = {
    # 'Спрощена закупівля': '&proc_type%5B0%5D=belowThreshold',
    # 'Відкриті торги з особливостями': '&proc_type%5B1%5D=aboveThreshold',
    # 'Відкриті торги': '&proc_type%5B2%5D=aboveThresholdUA',
    # 'Відкриті торги з публікацією англійською мовою': '&proc_type%5B3%5D=aboveThresholdEU',
    # 'Переговорна процедура': '&proc_type%5B4%5D=negotiation',
    # 'Переговорна процедура (скорочена)': '&proc_type%5B5%5D=negotiation.quick',
    # 'Переговорна процедура для потреб оборони': '&proc_type%5B6%5D=aboveThresholdUA.defense',
    # 'Конкурентний діалог 1-ий етап': '&proc_type%5B7%5D=competitiveDialogueUA',
    # 'Конкурентний діалог з публікацією англійською мовою 1-ий етап': '&proc_type%5B8%5D=competitiveDialogueEU',
    # 'Конкурентний діалог 2-ий етап': '&proc_type%5B9%5D=competitiveDialogueUA.stage2',
    # 'Конкурентний діалог з публікацією англійською мовою 2-ий етап': '&proc_type%5B10%5D=competitiveDialogueEU.stage2',
    # 'Закупівля без використання електронної системи': '&proc_type%5B11%5D=reporting',
    # 'Відкриті торги для закупівлі енергосервісу': '&proc_type%5B12%5D=esco',
    # 'Укладання рамкової угоди': '&proc_type%5B13%5D=closeFrameworkAgreementUA',
    # 'Відбір для закупівлі за рамковою угодою': '&proc_type%5B14%5D=closeFrameworkAgreementSelectionUA',
    # 'Запит ціни пропозицій': '&proc_type%5B15%5D=priceQuotation',
    # 'Спрощені торги із застосуванням електронної системи закупівель': '&proc_type%5B16%5D=simple.defense',
    'Спрощена закупівля': 'belowThreshold',
    'Відкриті торги з особливостями': 'aboveThreshold',
    'Відкриті торги': 'aboveThresholdUA',
    'Відкриті торги з публікацією англійською мовою': 'aboveThresholdEU',
    'Переговорна процедура': 'negotiation',
    'Переговорна процедура (скорочена)': 'negotiation.quick',
    'Переговорна процедура для потреб оборони': 'aboveThresholdUA.defense',
    'Конкурентний діалог 1-ий етап': 'competitiveDialogueUA',
    'Конкурентний діалог з публікацією англійською мовою 1-ий етап': 'competitiveDialogueEU',
    'Конкурентний діалог 2-ий етап': 'competitiveDialogueUA.stage2',
    'Конкурентний діалог з публікацією англійською мовою 2-ий етап': 'competitiveDialogueEU.stage2',
    'Закупівля без використання електронної системи': 'reporting',
    'Відкриті торги для закупівлі енергосервісу': 'esco',
    'Укладання рамкової угоди': 'closeFrameworkAgreementUA',
    'Відбір для закупівлі за рамковою угодою': 'closeFrameworkAgreementSelectionUA',
    'Запит ціни пропозицій': 'priceQuotation',
    'Спрощені торги із застосуванням електронної системи закупівель': 'simple.defense',
}

regions = {
    'Севастополь': '&region=99',
    'Луганська область': '&region=91-94',
    'місто Київ': '&region=1-6',
    'Запорізька область': '&region=69-72',
    'Харківська область': '&region=61-64',
    'Дніпропетровська область': '&region=49-53',
    'Полтавська область': '&region=36-39',
    'Донецька область': '&region=83-87',
    'Київська область': '&region=7-9',
    'Одеська область': '&region=65-68',
    'Херсонська область': '&region=73-75',
    'Миколаївська область': '&region=54-57',
    'Житомирська область': '&region=10-13',
    'Волинська область': '&region=43-45',
    'Львівська область': '&region=79-82',
    'Чернівецька область': '&region=58-60',
    'Черкаська область': '&region=18-20',
    'Сумська область': '&region=40-42',
    'Автономна Республіка Крим': '&region=95-98',
    'Кіровоградська область': '&region=25-28',
    'Закарпатська область': '&region=88-90',
    'Хмельницька область': '&region=29-32',
    'Чернігівська область': '&region=14-17',
    'Тернопільська область': '&region=46-48',
    'Івано-Франківська область': '&region=76-78',
    'Вінницька область': '&region=21-24',
    'Рівненська область': '&region=33-35',
}


def get_url(data):
    param = ''
    DK012_2015 = data[0]['ДК021:2015'].split(', ')
    Status = data[0]['Статус'].split(', ')
    Procurement_type = data[0]['Вид закупівлі'].split(', ')
    print(f'ДК021:2015 - {DK012_2015}, Статус - {Status}, Вид закупівлі - {Procurement_type}')

    for i in range(len(Status)):
        param += f'&status%5B{i}%5D={status[Status[i]]}'

    for i in range(len(Procurement_type)):
        param += f'&proc_type%5B{i}%5D={procurement_type[Procurement_type[i]]}'

    for i in range(len(DK012_2015)):
        param += f'&cpv%5B{i}%5D={DK012_2015[i]}'

    print('param', param)

    url = f'https://prozorro.gov.ua/api/search/tenders?filterType=tenders{param}&region=1-6'

    return url
