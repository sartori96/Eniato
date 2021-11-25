import requests
from flask import Flask
from bs4 import BeautifulSoup

provincias = requests.get("https://www.google.com/")

src = provincias.content

soup = BeautifulSoup(src, 'html.parser')

todosA = soup.find_all('a')

print(todosA)
#print(src)