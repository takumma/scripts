import requests
from bs4 import BeautifulSoup
import re

url = 'https://business.nikkei.com'
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')

elems = soup.find_all('span')

for elem in elems:
    try:
        string = elem.get('class').pop(0)
        if string in 'category':
            print(elem.string)
            title = elem.find_next_sibling('h3')
            print(title.text.replace('\n', ''))
            r = elem.find_previous('a')
            print(url + r.get('href'), '\n')
    except:
        pass
