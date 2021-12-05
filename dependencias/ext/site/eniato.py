# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

r = requests.get(
    "https://pc.saiteichingin.info/table/page_list_nationallist.php"
    )

soup = BeautifulSoup(r.text, 'html.parser')

mostra = soup.find('div', attrs={'class': 'industryTableArea_list'})

mostra = mostra.find('table')


#mostra = soup.findAll('td')
cidades = mostra.find_all('a')
salarios = mostra.find_all('td', {'class': 'money'})
datas = mostra.find_all('td', {'class': 'date'})
cidades_arr = []
salarios_arr = []
datas_arr = []
for c in cidades:
  cidades_arr.append(c.text)

for s in salarios:
  salarios_arr.append(s.text)

for d in datas:
  datas_arr.append(d.text)

serie_cidades = pd.Series(cidades_arr)
serie_salarios = pd.Series(salarios_arr)
serie_datas = pd.Series(datas_arr)


df_tabela = pd.concat([serie_cidades, serie_salarios, serie_datas], axis=1)
df_tabela.columns=['cidade', 'salario', 'atualizacao']
