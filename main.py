from cgitb import html
from unicodedata import name
from bs4 import BeautifulSoup
from matplotlib.pyplot import ticklabel_format, title
import requests
import re

from tomlkit import date

url = 'https://cloak.pia.jp/resale/item/list?eventCd=2209305&eventCd=2209306&eventCd=2209307&acptCliCd=ATM043&acptCliCd=ATM053&acptCliCd=ATM003&acptCliCd=ATM013&acptCliCd=ATM023&acptCliCd=ATM033&acptCliCd=ATM063&acptCliCd=ATM073'
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

#print(soup)
#elems = soup.select('#wrapper > div > div.item_result_wrapper > ol:nth-child(1) > div')
#elems = soup.find_all("a")

performance_name = soup.select(
    '#wrapper > div > div.item_result_wrapper > ol:nth-child(1) > div > a > h1'
)[0].contents[0]

performance_date = soup.select(
    '#wrapper > div > div.item_result_wrapper > ol:nth-child(1) > div > a > div.item_header.clearfix > div > p:nth-child(1)'
)[0].contents[0]

sheets = soup.select(
    '#wrapper > div > div.item_result_wrapper > ol:nth-child(1) > div > a > div.item_result_box_msg > span > span:nth-child(1)'
)[0].contents[0]

ticket = soup.select(
    '#wrapper > div > div.item_result_wrapper > ol:nth-child(1) > div > a > div.item_result_box_msg > p'
)[0].contents[0]

price = soup.select(
    '#wrapper > div > div.item_result_wrapper > ol:nth-child(1) > div > a > div.item_total > span:nth-child(2)'
)[0].contents[0]

print(performance_name)
print(performance_date)
print(ticket)
print(sheets)
print(price)