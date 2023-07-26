from .Prozorro_parser import get_json


def append_HTML(data_for_parser):
    data, total_tenders = get_json(data_for_parser)

    # Шаблон HTML-файла
    List_HTML_for_email = ['<!doctype html>\n', '<html lang="en">\n', '<head>\n', '    <meta charset="UTF-8">\n',
                           '    <meta name="viewport"\n',
                           '          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">\n',
                           '    <meta http-equiv="X-UA-Compatible" content="ie=edge">\n',
                           '    <title>Document</title>\n', '</head>\n', '<body>\n', '\n', '</body>\n', '</html>']

    i = 0
    for item in range(total_tenders):
        List_HTML_for_email.insert(10 + i, '<hr align="left" width="30%" color="black" size=1>\n')
        List_HTML_for_email.insert(11 + i, f'<p><a href="{data[item][6]}">{data[item][0]}</a></p>\n')
        List_HTML_for_email.insert(12 + i, f'<p>Місто: {data[item][1]}</p>\n')
        List_HTML_for_email.insert(13 + i, f'<p><strong>Компанія: </strong>{data[item][2]}</p>\n')
        List_HTML_for_email.insert(14 + i, f'<p><strong>ID: </strong>{data[item][3]}</p>\n')
        List_HTML_for_email.insert(15 + i, f'<p>Очікувана вартість: <strong>{data[item][4]} UAH</strong></p>\n')
        List_HTML_for_email.insert(16 + i, f'<p>Оголошено: {data[item][5]}</p>\n')
        i += 7

    with open("index.html", 'w', encoding='utf-8') as f:
        f.write(' '.join(List_HTML_for_email))

    print(total_tenders)


if __name__ == "__main__":
    append_HTML()
