import asyncio
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

from database.execute import update_id_ad
from database.fetch import url_for_new_ad, read_data_for_old_users
from loader import bot


# sending the first ad to the user and storing the ad id for further orientation
async def scraping_first_ad(id_user: int):
    result = await url_for_new_ad(id_user)

    req = requests.get(result[0].get('url')).text

    soup = BeautifulSoup(req, 'html.parser')
    id_first_ad = soup.find(class_=['ooa-1rudse5 eayvfn60', 'ooa-1g2kumr eayvfn60', 'ooa-yoaryb eayvfn60'])
    link = soup.find(class_='eayvfn66 eayvfn620 ooa-10p8u4x er34gjf0')
    try:
        data = [id_user, int(id_first_ad['id'])]
        await update_id_ad(data)
    except Exception as e:
        load_dotenv()
        await bot.send_message(chat_id=int(os.getenv("admin_id")), text=e)

    try:
        url = link.findChild("a")['href']
        if url:
            await bot.send_message(
                id_user,
                text=f'А вот и самое свежее объявление ;)\n\n{url}'
            )
    except:
        await bot.send_message(
            id_user,
            text='Редкая машинка, на данный момент нет ни одного объявления :('
        )


async def scraping_data():
    result = await read_data_for_old_users()

    for res in result:
        req = requests.get(res['url']).text
        soup = BeautifulSoup(req, 'html.parser')
        pars_id = soup.find_all(class_=['ooa-1rudse5 eayvfn60', 'ooa-1g2kumr eayvfn60', 'ooa-yoaryb eayvfn60'])

        id_list = []

        for item in pars_id:
            id_list.append(int(item['id']))

        if id_list and res['id_ad'] != id_list[0]:
            id_new = id_list[0]
            data = [res['id_user'], id_new]

            await update_id_ad(data)

        links = soup.find_all(class_='eayvfn66 eayvfn620 ooa-10p8u4x er34gjf0')
        urls = []

        for item in links:
            urls.append(item.findChild("a")['href'])

        try:
            dict_id_url = dict(zip(id_list, urls))

            for id, url in dict_id_url.items():
                # if so far there has not been a single announcement
                if res['id_ad'] == 0:
                    await bot.send_message(chat_id=res['id_user'], text=url)
                    data = [res['id_user'], id]
                    await update_id_ad(data)
                    break
                # send ads until its id matches the id of the very first sent ad
                elif id != res['id_ad']:
                    await bot.send_message(chat_id=res['id_user'], text=url)

                else:
                    break

        except Exception as e:
            load_dotenv()
            await bot.send_message(chat_id=int(os.getenv("admin_id")), text=e)

        await asyncio.sleep(1)
