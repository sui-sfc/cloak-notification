from cgitb import html
from bs4 import BeautifulSoup
from matplotlib.pyplot import title
import requests
import re

from tomlkit import date

url = 'https://cloak.pia.jp/resale/item/list?eventCd=2209305&eventCd=2209306&eventCd=2209307&acptCliCd=ATM043&acptCliCd=ATM053&acptCliCd=ATM003&acptCliCd=ATM013&acptCliCd=ATM023&acptCliCd=ATM033&acptCliCd=ATM063&acptCliCd=ATM073'
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

#print(soup)
#elems = soup.select('#wrapper > div > div.item_result_wrapper > ol:nth-child(1) > div')
#elems = soup.find_all("a")

title = soup.find('h1', class_='item_title')
date = soup.select(
    '#wrapper > div > div.item_result_wrapper > ol:nth-child(1) > div > a > div.item_header.clearfix > div > p:nth-child(1)')
title = title.contents[0]
date = date[0].contents[0]
