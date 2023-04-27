from database.execute import insert_update_data


async def create_url(data_for_create_url: dict = None):
    false_answer = 'Без разницы'

    id_user = data_for_create_url['id_user']

    mark = data_for_create_url['mark'].lower()

    model = data_for_create_url['model'].lower().replace(' ', '-')

    transmission = data_for_create_url['transmission']
    if transmission == 'Автомат':
        transmission = 'automatic'
    elif transmission == 'Ручная':
        transmission = 'manual'

    year_min = data_for_create_url['year_min']
    if year_min == false_answer:
        year_min = 1900
    else:
        year_min = int(year_min)

    year_max = data_for_create_url['year_max']
    if year_max == false_answer:
        year_max = 2023
    else:
        year_max = int(year_max)

    mileage_min = data_for_create_url['mileage_min']
    if mileage_min == false_answer:
        mileage_min = 0
    else:
        mileage_min = int(mileage_min)

    mileage_max = data_for_create_url['mileage_max']
    if mileage_max == false_answer:
        mileage_max = 2000000
    else:
        mileage_max = int(mileage_max)

    price_min = data_for_create_url['price_min']
    if price_min == false_answer:
        price_min = 0
    else:
        price_min = int(price_min)

    price_max = data_for_create_url['price_max']
    if price_max == false_answer:
        price_max = 4000000
    else:
        price_max = int(price_max)

    # the presence of the "gearbox" criterion affects the structure of the link, so if/else is used
    if transmission == false_answer:
        url_request = f'https://www.otomoto.pl/osobowe/{mark}/{model}/od-{int(year_min)}' \
                      f'?search%5Bfilter_float_year%3Ato%5D={int(year_max)}&search%5Bfilter_float_mileage%3Afrom%5D=' \
                      f'{int(mileage_min)}&search%5Bfilter_float_mileage%3Ato%5D={int(mileage_max)}' \
                      f'&search%5Bfilter_float_price%3Afrom%5D={int(price_min)}&search%5Bfilter_float_price%3Ato%5D=' \
                      f'{int(price_max)}&search%5Border%5D=created_at_first%3Adesc&search%' \
                      f'5Badvanced_search_expanded%5D=true'

    else:
        url_request = f'https://www.otomoto.pl/osobowe/{mark}/{model}/od-{int(year_min)}' \
                      f'?search%5Bfilter_float_year%3Ato%5D={int(year_max)}&search%5Bfilter_float_mileage%3Afrom%5D=' \
                      f'{int(mileage_min)}&search%5Bfilter_float_mileage%3Ato%5D={int(mileage_max)}' \
                      f'&search%5Bfilter_float_price%3Afrom%5D={int(price_min)}&search%5Bfilter_float_price%3Ato%5D=' \
                      f'{int(price_max)}&search%5Bfilter_enum_gearbox%5D={transmission}&search%5Border%' \
                      f'5D=created_at_first%3Adesc&search%5Badvanced_search_expanded%5D=true'

    data = [
        id_user,
        mark,
        model,
        transmission,
        year_min,
        year_max,
        mileage_min,
        mileage_max,
        price_min,
        price_max,
        url_request
    ]

    await insert_update_data(data)
