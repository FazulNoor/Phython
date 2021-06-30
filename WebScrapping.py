from bs4 import BeautifulSoup
import requests
import csv

soup = BeautifulSoup(requests.get("https://en.wikipedia.org/wiki/Main_Page").text, 'lxml')

#<div id="mp-welcome">Welcome to <a href="/wiki/Wikipedia" title="Wikipedia">Wikipedia</a>,</div>
h1 = soup.find('div', {"id" :'mp-welcome'})

text = h1.text

print(text)

