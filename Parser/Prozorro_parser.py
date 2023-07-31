import requests
from .options import get_url


def get_json(data_for_parser):
    print('Parser data', data_for_parser)
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/98.0.4758.82 Safari/537.36",
    }
    list_data = []

    print('url', get_url(data_for_parser))
    # url = "https://prozorro.gov.ua/api/search/tenders?filterType=tenders&status%5B0%5D=active.enquiries&status%5B1%5D=active.tendering&cpv%5B0%5D=71630000-3&cpv%5B1%5D=73110000-6&cpv%5B2%5D=50410000-2&page=1&region=1-6"
    url = get_url(data_for_parser)
    # Получаем JSON файл
    session = requests.session()
    response = session.post(url=url, headers=headers)
    data = response.json()
    # Количество тендеров на 1й странице
    quantity_tender_in_page = data['per_page']
    # Всего тендеров
    total_tenders = data["total"]
    print('total_tenders -', total_tenders)

    if total_tenders >= 500:
        pass

    if total_tenders <= quantity_tender_in_page:
        page = 1
    else:
        page = total_tenders // quantity_tender_in_page + 1
    try:
        for item in range(1, page + 1):
            print("==============================================================================================")
            print(item)
            # url_page = f"https://prozorro.gov.ua/api/search/tenders?filterType=tenders&status%5B0%5D=active.enquiries&status%5B1%5D=active.tendering&cpv%5B0%5D=71630000-3&cpv%5B1%5D=73110000-6&cpv%5B2%5D=50410000-2&page=1&region=1-6&page={item}"
            url_page = f"{url}&page={item}"
            session = requests.session()
            response = session.post(url=url_page, headers=headers)
            data_page = response.json()
            for tender in range(quantity_tender_in_page):
                title = data_page["data"][tender]["title"]
                try:
                    city_company = data_page["data"][tender]["procuringEntity"]["address"]["locality"]
                except Exception as error:
                    city_company = data_page["data"][tender]["procuringEntity"]["address"]["region"]

                name_company = data_page["data"][tender]["procuringEntity"]["identifier"]["legalName"]
                ID_tender = data_page["data"][tender]["tenderID"]
                price = data_page["data"][tender]["value"]["amount"]
                try:
                    start_date = data_page["data"][tender]["enquiryPeriod"]["startDate"][:10]
                except Exception as error:
                    start_date = 'Дати проведення ще немає'
                link = (f"https://prozorro.gov.ua/tender/{ID_tender}")
                print("---------------------------------------------------------------------------------------")
                list_data += [[title, city_company, name_company, ID_tender, price, start_date, link]]
                print(tender)
                print(title, '\n', city_company, '\n', name_company, '\n', ID_tender,
                      '\n', price, '\n', start_date, '\n', link)
                print("---------------------------------------------------------------------------------------")
    except Exception as ex:
        print('Something went wrong')
        print(f'Error{ex}')
    return list_data, total_tenders


def main():
    get_json()


if __name__ == "__main__":
    main()
