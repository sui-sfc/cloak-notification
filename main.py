import json
from time import time
import get_info
import discord
import tokens
from discord.ext import tasks


#ファイル保存
def f_write(ticket_info):
    tf = open("latest_ticket.json", "w")
    json.dump(ticket_info, tf)
    tf.close()

#ファイル読み出し
def f_read():
    tf = open("latest_ticket.json", "r")
    latest_data = json.load(tf)
    tf.close()
    return latest_data

#メッセージ作成
def s_message(ticket_info):
    tmp = []
    for i in ticket_info.keys():
        tmp.append(ticket_info.get(i))
        message = '\n'.join(tmp)
    return message

    
url = tokens.url()
TOKEN = tokens.token()

client = discord.Client()



async def SendMessage(ticket_info):
    await client.get_channel(tokens.ch()).send(s_message(ticket_info))


@client.event
async def on_ready():
    print('ログイン') 
    ticket_info = get_info.get_cloak_ticket_info(url, 1)
    await SendMessage(ticket_info)
    f_write(ticket_info)
    print('run')
    timeloop.start()

  

@tasks.loop(seconds=30)
async def timeloop():
    print('test')
    latast_data = f_read()
    ticket_info = get_info.get_cloak_ticket_info(url, 1)
    if latast_data == ticket_info:
        pass
    else:
       await SendMessage(ticket_info)



client.run(TOKEN)
