import sys
from tkinter import filedialog, messagebox
from telethon.sync import TelegramClient
from telethon.tl.functions.contacts import GetContactsRequest
import configparser
from tkinter import *

import os
def sendmycode(mycode,root,phone):
    client.sign_in(phone,mycode)
    root.quit()    
def sendcode(phone):
    root = Tk()
    root.title('Telegram Bot')
    root.geometry('500x120+500+200')
    coedext=Label(root,text="Enter the code",font="Verdana 12 bold").place(x=10,y=10)
    mycode=Entry(root,width=25,font="Verdana 12 bold")
    mycode.place(x=170,y=10)
    Login=Button(root,text="Save",command=lambda :sendmycode(mycode.get(),root,phone),width=25,height=2,font="Verdana 12 bold")
    Login.place(x=170,y=50)
    root.mainloop()
os.system("""python -m pip install PyMySQL""")
import pymysql.cursors
db = pymysql.connect(host='185.136.84.129', #'185.136.84.129',
                             user='maydryco_telegraf',#'maydryco_telegraf',
                             password='Telgraf33!',#'Telgraf33!',
                             db='maydryco_telegraf',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
baglanti = db.cursor()
userid="erol"
sql="SELECT * FROM users WHERE apiid=%s"
baglanti.execute(sql,userid)
exist = baglanti.fetchone()
if exist is None:
    newsql="INSERT INTO users (apiid) VALUES (%s)"
    baglanti.execute(newsql, (userid))
    db.commit()
baglanti.close()   
if exist["search_key"] is None:
    messagebox.showwarning("Telegram Bot","Please Buy Program")
    #sys.exit(1)
try:
    file = open('config.data', 'r')
except IOError:
   import auth as Auth
cpass = configparser.RawConfigParser()
cpass.read('config.data')
api_id = cpass['cred']['id']
api_hash = cpass['cred']['hash']
phone = cpass['cred']['phone']
client = TelegramClient(phone, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    sendcode(phone)
result = client(GetContactsRequest(hash=client.get_me().access_hash))
import sqlite3
sq = sqlite3.connect('userlist.db')
komut = "CREATE TABLE IF NOT EXISTS userlist(u_username, u_user_id,u_access_hash,u_name)"
imlec = sq.cursor()
imlec.execute(komut)
sq.commit()
komut2="DELETE FROM userlist"
imlec.execute(komut2)
sq.commit()
for i in range(len(result.users)):
        username = result.users[i].username or ""
        first_name = result.users[i].first_name or ""
        last_name = result.users[i].last_name or ""
        name= (first_name + ' ' + last_name).strip()
        komut = "INSERT INTO userlist VALUES (?,?,?,?)"
        imlec.execute(komut,(username,result.users[i].id,result.users[i].access_hash,name))
        sq.commit()
sq.close()

import tkinter as tk
from tkinter import filedialog

root=tk.Tk()    

ent1=tk.Entry(root,font=40)
ent1.grid(row=2,column=2)

def browsefunc():
    filename =filedialog.askopenfilename(initialdir="",filetypes=(("tiff files","*.tiff"),("All files","*.*")))
    ent1.insert(tk.END, filename) # add this

b1=tk.Button(root,text="DEM",font=40,command=browsefunc)
b1.grid(row=2,column=4)

root.mainloop()