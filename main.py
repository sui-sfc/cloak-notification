from cgitb import html
from unicodedata import name
from bs4 import BeautifulSoup
import get_info
import re

from tomlkit import date

url = 'https://cloak.pia.jp/resale/item/list?eventCd=2209305&eventCd=2209306&eventCd=2209307&acptCliCd=ATM043&acptCliCd=ATM053&acptCliCd=ATM003&acptCliCd=ATM013&acptCliCd=ATM023&acptCliCd=ATM033&acptCliCd=ATM063&acptCliCd=ATM073'




performance_name,performance_date,ticket,sheets,price = get_info.get_cloak_ticket_info(url,1)

print(performance_name)
print(performance_date)
print(ticket)
print(sheets)
print(price)
