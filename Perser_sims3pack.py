import json
import random
import time

import requests
from bs4 import BeautifulSoup
import fake_useragent


user = fake_useragent.UserAgent().random
header = {'user-agent':user}
number = 1

for i in range(666):
    url = (f'https://sims3pack.ru/odezhda-dlya-sims-3/page/{i}/')
    res = requests.get(url, headers=header)
    soup = BeautifulSoup(res.text, 'lxml')
    item = soup.find('div', class_='content-wrap')
    items = item.find_all('div', class_='base shortstory')
    for predmet in items:
        urls = predmet.find('a').get('href')
        res = requests.get(urls, headers=header)
        soup = BeautifulSoup(res.text, 'lxml')
        itt = soup.find('div',class_='base fullstory')
        item = itt.find('div',class_='files_download')
        url_sims = item.find('a').get('href')
        butes = requests.get(f'{url_sims}').content
        rar = False
        try:
            with open(f'C:\sims3\{number}.sims3pack', 'wb') as file:
                file.write(butes)
            rar = True
        except BaseException:
            print('не то')
        if rar == False:
            try:
                with open(f'C:\sims3\{number}.zip', 'wb') as file:
                    file.write(butes)
            except BaseException:
                print('что то странное ')
        number +=1
