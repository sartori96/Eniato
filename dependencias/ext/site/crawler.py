import requests
from bs4 import BeautifulSoup
import numpy as np

def crawler():

    soup = BeautifulSoup(requests.get("https://pc.saiteichingin.info/table/page_list_nationallist.php").content, 'html.parser')

    mostra = soup.find('div', attrs={'class': 'industryTableArea_list'})

    #lista ={}
    #for tr in mostra.select('tr'):
    #    lista.update({tr.find('a'): tr.find('td', attrs={'class':'money'})})
    #    
    #


    lista =[]
    for tr in mostra.select('td', attrs={'a'}):
        lista.append(tr.text.strip())





    #alt
    #lista =[]
    #for tr in mostra.select('tr'):
    #    lista.append(tr.text.strip())

    #lista.pop(0)
    #print(lista)

    #for x in lista:
    #    print (x)
    print(lista)
    return lista