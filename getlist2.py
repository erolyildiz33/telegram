import telethon
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import os, sys
import configparser
import csv
import time
import json
import os
import sys
import time
import random
from random import randint
from telethon import TelegramClient
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.tl.functions.contacts import GetContactsRequest

from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.types import InputPeerUser


re = "\033[1;31m"
gr = "\033[1;32m"
cy = "\033[1;36m"
searc_param="Uygar"

def banner():
    print(f"""
{re}╔╦╗{cy}┌─┐┬  ┌─┐{re}╔═╗  ╔═╗{cy}┌─┐┬─┐┌─┐┌─┐┌─┐┬─┐
{re} ║ {cy}├┤ │  ├┤ {re}║ ╦  ╚═╗{cy}│  ├┬┘├─┤├─┘├┤ ├┬┘
{re} ╩ {cy}└─┘┴─┘└─┘{re}╚═╝  ╚═╝{cy}└─┘┴└─┴ ┴┴  └─┘┴└─
            version : 3.1
        youtube.com/theunknon
        """)


cpass = configparser.RawConfigParser()
cpass.read('config.data')

try:
    api_id = cpass['cred']['id']
    api_hash = cpass['cred']['hash']
    phone = cpass['cred']['phone']
    client = TelegramClient(phone, api_id, api_hash)
except KeyError:
    os.system('clear')
    banner()
    print(re + "[!] run python3 setup.py first !!\n")
    sys.exit(1)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    os.system('clear')
    banner()
    client.sign_in(phone, input(gr + '[+] Enter the code: ' + re))


banner()
myusers = []
last_date = None
chunk_size = 200
groups = []

result = client(GetContactsRequest(hash=client.get_me().access_hash))
#print(type(result))
#result = client(functions.contacts.GetContactsRequest(hash=-12398745604826))



with open("contacts2.csv","w",encoding='UTF-8') as f:
    writer = csv.writer(f,delimiter=",",lineterminator="\n")
    writer.writerow(['username','user id', 'access hash','name'])
    for i in range(len(result.users)):
        if str(result.users[i].first_name).find(searc_param) != -1 or str(result.users[i].last_name).find(searc_param) != -1:
            username = result.users[i].username or ""
            first_name = result.users[i].first_name or ""
            last_name = result.users[i].last_name or ""
            name= (first_name + ' ' + last_name).strip()
            writer.writerow([username,result.users[i].id,result.users[i].access_hash,name])
print('Members scraped successfully!')