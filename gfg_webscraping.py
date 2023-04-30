# import requests
# from bs4 import BeautifulSoup

# req=requests.get('https://www.geeksforgeeks.org/')
# soup =BeautifulSoup(req.content,"html.parser")

# print(soup.get_text())


import requests
from bs4 import BeautifulSoup
import json
import re

def countwords(url):
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    
    word = soup.get_text()
    words = re.findall(r'\b[a-zA-Z]+\b', word)

    
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    
    jsondata = json.dumps(freq)

    
    return jsondata

url = 'https://www.geeksforgeeks.org/'
jsondata = countwords(url)
print(jsondata)