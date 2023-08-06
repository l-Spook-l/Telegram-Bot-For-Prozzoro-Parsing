status = {
    'період уточнень': 'active.enquiries',
    'подання пропозицій': 'active.tendering',
    'прекваліфікація': 'active.pre-qualification',
    'прекваліфікація (період оскарження)': 'active.pre-qualification.stand-still',
    'аукціон': 'active.auction',
    'кваліфікація переможця': 'active.qualification',
    'кваліфікація переможця (період оскарження)': 'active.qualification.stand-still',
    'пропозиції розглянуті': 'active.awarded',
    'торги не відбулися': 'unsuccessful',
    'торги відмінено': 'cancelled',
    'завершена': 'complete',
    'підготовка угоди': 'active',
    'підготовка до 2-го етапу': 'active.stage2.pending',
    'створення 2-го етапу': 'active.stage2.waiting',
}


procurement_type = {
    'спрощена закупівля': 'belowThreshold',
    'відкриті торги з особливостями': 'aboveThreshold',
    'відкриті торги': 'aboveThresholdUA',
    'відкриті торги з публікацією англійською мовою': 'aboveThresholdEU',
    'переговорна процедура': 'negotiation',
    'переговорна процедура (скорочена)': 'negotiation.quick',
    'переговорна процедура для потреб оборони': 'aboveThresholdUA.defense',
    'конкурентний діалог 1-ий етап': 'competitiveDialogueUA',
    'конкурентний діалог з публікацією англійською мовою 1-ий етап': 'competitiveDialogueEU',
    'конкурентний діалог 2-ий етап': 'competitiveDialogueUA.stage2',
    'конкурентний діалог з публікацією англійською мовою 2-ий етап': 'competitiveDialogueEU.stage2',
    'закупівля без використання електронної системи': 'reporting',
    'відкриті торги для закупівлі енергосервісу': 'esco',
    'укладання рамкової угоди': 'closeFrameworkAgreementUA',
    'відбір для закупівлі за рамковою угодою': 'closeFrameworkAgreementSelectionUA',
    'запит ціни пропозицій': 'priceQuotation',
    'спрощені торги із застосуванням електронної системи закупівель': 'simple.defense',
}

regions = {
    'севастополь': '&region=99',
    'луганська область': '&region=91-94',
    'місто Київ': '&region=1-6',
    'запорізька область': '&region=69-72',
    'харківська область': '&region=61-64',
    'дніпропетровська область': '&region=49-53',
    'полтавська область': '&region=36-39',
    'донецька область': '&region=83-87',
    'київська область': '&region=7-9',
    'одеська область': '&region=65-68',
    'херсонська область': '&region=73-75',
    'миколаївська область': '&region=54-57',
    'житомирська область': '&region=10-13',
    'волинська область': '&region=43-45',
    'львівська область': '&region=79-82',
    'чернівецька область': '&region=58-60',
    'черкаська область': '&region=18-20',
    'сумська область': '&region=40-42',
    'крим': '&region=95-98',
    'кіровоградська область': '&region=25-28',
    'закарпатська область': '&region=88-90',
    'хмельницька область': '&region=29-32',
    'чернігівська область': '&region=14-17',
    'тернопільська область': '&region=46-48',
    'івано-франківська область': '&region=76-78',
    'вінницька область': '&region=21-24',
    'рівненська область': '&region=33-35',
}


async def get_url(data):
    list_url = []
    for i in range(len(data)):
        filters = ''
        DK012_2015 = data[i]['ДК021:2015'].split(', ')
        Status = data[i]['Статус'].split(', ')
        Procurement_type = data[i]['Вид закупівлі'].split(', ')
        Region = data[i]['Регіон']

        if Status[0] != 'пропустити':
            for id in range(len(Status)):
                filters += f'&status%5B{id}%5D={status[Status[id]]}'

        if Procurement_type[0] != 'пропустити':
            for id in range(len(Procurement_type)):
                filters += f'&proc_type%5B{id}%5D={procurement_type[Procurement_type[id]]}'

        if DK012_2015[0] != 'пропустити':
            for id in range(len(DK012_2015)):
                filters += f'&cpv%5B{id}%5D={DK012_2015[id]}'

        if Region[0] != 'пропустити':
            filters += regions[Region]

        url = f'https://prozorro.gov.ua/api/search/tenders?filterType=tenders{filters}'
        list_url.append(url)

    return list_url
