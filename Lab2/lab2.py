import requests


def current_weather_moscow():
    response = requests.get(
        'https://api.open-meteo.com/v1/forecast?latitude=55.7522&longitude=37.6156&current=temperature_2m').json()
    print(f'Текущая температура в Москве:\n{response['current']['temperature_2m']}°C')


def currency_exchange():
    response1 = requests.get(
        'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd/rub.json').json()
    response2 = requests.get(
        'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/cny/rub.json').json()
    response3 = requests.get(
        'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/eur/rub.json').json()
    print(f'Текущий курс валют:\nUSD: {response1['rub']}р\nCYN: {response2['rub']}р\n'
          f'EUR: {response3['rub']}р')


# Я не нашёл где в запросе отображается количество товара на складе, поэтому вывожу количество оценок товара
def shop_info():
    response = requests.get('https://fakestoreapi.com/products').json()
    item_list = []
    price_list = []
    rate_list = []
    rate_count_list = []
    for item in response:
        item_list.append(item['title'])
        price_list.append(item['price'])
        rate_list.append(item['rating']['rate'])
        rate_count_list.append(item['rating']['count'])
    print('Самые дорогие товары:')
    shop_help_func(response, price_list)

    print('\nТовары с самой высокой оценкой:')
    shop_help_func(response, rate_list)

    print('\nТовары с самым большим количеством оценок:')
    shop_help_func(response, rate_count_list)

    with open('item_titles.txt', mode='w', encoding='utf-8') as file:
        for item in sorted(item_list):
            file.write(item + '\n')


def shop_help_func(response, item_list):
    max_count = max(item_list)
    max_count_index = [x[0] for x in enumerate(item_list) if x[1] == max_count]
    for i in max_count_index:
        print(response[i]['title'])


def organisation_search():
    org_name = input('Введите название организации: ')
    # org_name = 'ВятГУ'
    response = requests.get(f'https://search-maps.yandex.ru/v1/?text={org_name}&type=biz&lang=ru_RU&'
                            f'apikey=85a285fc-11d2-4ba9-a37d-8154903e726c').json()
    for item in response['features']:
        print(f'Название: {item['properties']['name']}')
        print(f'Адрес: {item['properties']['description']}')
        print(f'Номер телефона: {item['properties']['CompanyMetaData']['Phones'][0]['formatted']}\n')


if __name__ == '__main__':
    current_weather_moscow()
    currency_exchange()
    shop_info()
    organisation_search()
