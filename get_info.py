from bs4 import BeautifulSoup
import requests
import time

#cloakの番目のチケットを取得
def get_cloak_ticket_info(url,n):
    n = str(n)
    while(1):
        try:  
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")
            performance_name = soup.select(
                '#wrapper > div > div.item_result_wrapper > ol:nth-child(' + n+ 
                ') > div > a > h1'
            )[0].contents[0]

            performance_date = soup.select(
                '#wrapper > div > div.item_result_wrapper > ol:nth-child('+ n +
                ') > div > a > div.item_header.clearfix > div > p:nth-child(1)'
            )[0].contents[0]

            sheets = soup.select(
                '#wrapper > div > div.item_result_wrapper > ol:nth-child('+ n +
                ') > div > a > div.item_result_box_msg > span > span:nth-child(1)'
            )[0].contents[0]

            ticket = soup.select(
                '#wrapper > div > div.item_result_wrapper > ol:nth-child('+ n +
                ') > div > a > div.item_result_box_msg > p'
            )[0].contents[0]

            price = soup.select(
                '#wrapper > div > div.item_result_wrapper > ol:nth-child(' + n +
                ') > div > a > div.item_total > span:nth-child(2)'
            )[0].contents[0]
            break
        except IndexError:
            continue
            #time.sleep(5)
    return performance_name, performance_date, sheets, ticket, price
