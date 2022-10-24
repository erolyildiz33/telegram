from msilib.schema import AppId
from queue import Empty
from tkinter import *
from tkinter import messagebox
import os


def login():
    while apiId.get()=='' or hashNo.get()=='' or phone.get()=='' :
        messagebox.showerror("Telegram Bot","Please fill in all required fields")
        return
    os.system("""
		pip3 install telethon requests configparser
		python3 -m pip install telethon requests configparser
		touch config.data
		""")
    import configparser
    cpass = configparser.RawConfigParser()
    cpass.add_section('cred')
    cpass.set('cred', 'id', int(apiId.get()))
    cpass.set('cred', 'hash', hashNo.get())
    cpass.set('cred', 'phone', phone.get())
    setup = open('config.data', 'w')
    cpass.write(setup)
    setup.close()
    root.quit()
    

root = Tk()
root.title('Telegram Bot')
root.geometry('500x200+500+200')
apidTxt=Label(root,text="Api ID",font="Verdana 12 bold").place(x=10,y=10)
apiId=Entry(root,width=25,font="Verdana 12 bold")
apiId.place(x=170,y=10)
hashTxt=Label(root,text="Hash Code",font="Verdana 12 bold").place(x=10,y=50)
hashNo=Entry(root,width=25,font="Verdana 12 bold")
hashNo.place(x=170,y=50)
phoneTxt=Label(root,text="Phone Numaber",font="Verdana 12 bold").place(x=10,y=90)
phone=Entry(root,width=25,font="Verdana 12 bold")
phone.place(x=170,y=90)
Login=Button(root,text="Login",command=lambda :login(),width=25,height=2,font="Verdana 12 bold")
Login.place(x=170,y=120)     

root.mainloop() 
