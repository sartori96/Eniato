import requests
from bs4 import BeautifulSoup
import numpy as np

def crawler():

    soup = BeautifulSoup(requests.get("https://pc.saiteichingin.info/table/page_list_nationallist.php").content, 'html.parser')

    mostra = soup.find('div', attrs={'class': 'industryTableArea_list'})

    lista =[]
    for tr in mostra.select('td', attrs={'a'}):
        lista.append(tr.text.strip())
    return lista