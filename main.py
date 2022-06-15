import json
import get_info

url = 'https://cloak.pia.jp/resale/item/list?eventCd=2209305&eventCd=2209306&eventCd=2209307&acptCliCd=ATM043&acptCliCd=ATM053&acptCliCd=ATM003&acptCliCd=ATM013&acptCliCd=ATM023&acptCliCd=ATM033&acptCliCd=ATM063&acptCliCd=ATM073'

ticket_info = get_info.get_cloak_ticket_info(url,1)

#ファイル保存
tf = open("latest_ticket.json", "w")
json.dump(ticket_info, tf)
tf.close()

#ファイル読み出し
tf = open("latest_ticket.json", "r")
latest_data = json.load(tf)
tf.close

if latest_data == ticket_info:
    print('not update')
else: 
    print('update')
