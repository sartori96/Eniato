import requests
import re
from flask import Flask
from bs4 import BeautifulSoup

provincias = requests.get("https://pc.saiteichingin.info/table/page_list_nationallist.php")

src = provincias.content

soup = BeautifulSoup(src, 'html.parser')

mostra = soup.find('div', attrs={'class': 'industryTableArea_list'})

#target_content = soup.find('td', attrs={'class': 'money'})

#dt = target_content.find('td').get_text()

print(mostra)