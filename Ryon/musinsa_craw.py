import requests
from bs4 import BeautifulSoup

# https://m.store.musinsa.com/app/product/detail/1588267/0
# https://m.store.musinsa.com/app/product/detail/1588268/0


URL = 'https://m.store.musinsa.com/app/product/detail/1588267/0'

response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')

print(soup)