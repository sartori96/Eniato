import requests
from flask import Flask
from bs4 import BeautifulSoup

soup = BeautifulSoup(requests.get("https://pc.saiteichingin.info/table/page_list_nationallist.php").content, 'html.parser')

mostra = soup.find('div', attrs={'class': 'industryTableArea_list'})

lista =[]
for tr in mostra.select('tr'):
    lista.append(tr.text.strip())

lista.pop(0)
print(soup)
