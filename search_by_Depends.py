from ast import Delete
from asyncio import events
from asyncore import read
from cProfile import label
from cgitb import html, text
from cmath import e
from hashlib import new
from html.entities import html5
import readline
from tkinter import *
from tkinter import messagebox
from tokenize import Number
from turtle import title  
import tkinter as tk
import tkinter.filedialog
import os, shutil #редактирование файла
import re
#from unicodedata import name
from tkinter import scrolledtext
import pymongo
import json
from bs4 import BeautifulSoup
import functools
import hyperlink
def BDconect():
 try: 
  with open("log.txt", "r") as f:
   sd = f.readline().split()
   sf = f.readline().split()
   sz = f.readline().split()
  f.close() 
  username =str(sd)
  Password=str(sf)
  Address= str(sz)
  username =username.replace("['","")
  Password=Password.replace("['","")
  Address= Address.replace("['","")
  username =username.replace("']","")
  Password=Password.replace("']","")
  Address= Address.replace("']","")
  print(username)
  print(Password)
  print(Address)
  print()
  from pymongo import MongoClient
  if username != "" or Password != "" or Address != "":
   text = Address
   text = text.replace("user", username )
   text = text.replace("<password>", Password)
   print(text)
   cluster = MongoClient(text)
   global db
   db = cluster["Package"]
   global collection
   collection=db["package"]
  # messagebox.showinfo("Ошибка","\nНет подключения к серверу. Проверьте введённые данные\n")
  else:
    messagebox.showerror("Ошибка","\nНет подключения к серверу. Откройте меню настройки и выберите пункт сервер и введите данные о сервере\n")
 except FileNotFoundError:
    messagebox.showerror("Ошибка","\nНет подключения к серверу. Откройте меню настройки и выберите пункт сервер и введите данные о сервере\n") 
def btn_bd2(): # поиск по зависимостям
 def clu(event):
    def namepac1(event):
      click_point = "@%s,%s" % (event.x, event.y)
      trs = txtd3.tag_ranges("likes")
      Textdb = ""
      # определяется, на какой участок пришелся щелчок мыши, и берется
      # соответствующий ему URL
      for i in range(0, len(trs), 1):
        if txtd3.compare(trs[i], "<=", click_point) and \
          txtd3.compare(click_point, "<=", trs[i+1]):
          Textdb = txtd3.get(trs[i], trs[i+1])
      # Prinr.delete("1.0", END)
      print(Textdb)
      txtd3.delete(1.0, END)
      Packagedepens_label.config(text=Textdb)
      Textdb = Textdb.replace(" ",'')
      Textdb = Textdb.replace("(",' ')
      Textdb = Textdb.replace("=",'')
      Textdb = Textdb.replace(")",'')
      if  " " in Textdb:
        if  "<" in Textdb or  ">" in Textdb:
          Textdb = Textdb.replace("<",'')
          Textdb = Textdb.replace(">",'')
          a,b=Textdb.split()
          number1 = collection.count_documents({'Package': {'$regex': a}})
          if number1==0:
            txtd3.insert(INSERT,'Даного пакета нет в базе данных')
          else:  
            print('Ok')
          for channel in collection.find({'Package': {'$regex': a}}):
            bq=channel['Package']
            Bw=channel['Version']
            be=channel['Architecture']
            if 'Depends' in channel:
              br=channel['Depends']
              txtd3.insert(INSERT,'Package:'+' '+bq+'\n')
              txtd3.insert(INSERT,'Version:'+' '+Bw+'\n')
              txtd3.insert(INSERT,'Architecture:'+' '+be+'\n')
              txtd3.insert(INSERT,'Depends:'+' ')
              for frag in br: 
                if  "," in frag or  "|" in frag:
                  txtd3.insert(INSERT, frag) 
                else:
                  txtd3.insert(INSERT, frag,"likes")
              if 'PreDepends' in channel:
                ba=channel['PreDepends']
                txtd3.insert(INSERT,"\n"+'PreDepends:'+' ')  
                for frag1 in ba: 
                  if  "," in frag1 or  "|" in frag1:
                    txtd3.insert(INSERT, frag1)
                  else:
                    txtd3.insert(INSERT, frag1,"likes")  
            else: 
              if 'PreDepends' in channel:
                ba=channel['PreDepends']
                txtd3.insert(INSERT,'Package:'+' '+bq+'\n')
                txtd3.insert(INSERT,'Version:'+' '+Bw+'\n')
                txtd3.insert(INSERT,'Architecture:'+' '+be+'\n')  
                txtd3.insert(INSERT,'PreDepends:'+' ')  
                for frag1 in ba: 
                  if  "," in frag1 or  "|" in frag1:
                    txtd3.insert(INSERT, frag1)
                  else:
                    txtd3.insert(INSERT, frag1,"likes")  
              else:         
                txtd3.insert(INSERT,'Package:'+' '+bq+'\n')
                txtd3.insert(INSERT,'Version:'+' '+Bw+'\n')
                txtd3.insert(INSERT,'Architecture:'+' '+be)   
            txtd3.insert(INSERT,'\n'+'\n')
            txtd3.tag_config("likes", foreground='#d2d2d2', underline=1) 
          txtd3.tag_bind("likes", "<1>",namepac1)
        else:  
          a,b=Textdb.split()
          print(Textdb)
          print(a)
          print(b)
          number1 = collection.count_documents({'$and': [{'Package': a},{'Version': b}]})
          if number1==0:
            txtd3.insert(INSERT,'Даного пакета нет в базе данных')
          else:  
            print('Ok')
          for channel in collection.find({'$and': [{'Package': a},{'Version': b}]}):
            bq=channel['Package']
            Bw=channel['Version']
            be=channel['Architecture']
            if 'Depends' in channel:
              br=channel['Depends']
              txtd3.insert(INSERT,'Package:'+' '+bq+'\n')
              txtd3.insert(INSERT,'Version:'+' '+Bw+'\n')
              txtd3.insert(INSERT,'Architecture:'+' '+be+'\n')
              txtd3.insert(INSERT,'Depends:'+' ')
              for frag in br: 
                if  "," in frag or  "|" in frag:
                  txtd3.insert(INSERT, frag) 
                else:
                  txtd3.insert(INSERT, frag,"likes")
              if 'PreDepends' in channel:
                ba=channel['PreDepends']
                txtd3.insert(INSERT,"\n"+'PreDepends:'+' ')  
                for frag1 in ba: 
                  if  "," in frag1 or  "|" in frag1:
                    txtd3.insert(INSERT, frag1)
                  else:
                    txtd3.insert(INSERT, frag1,"likes")  
            else: 
              if 'PreDepends' in channel:
                ba=channel['PreDepends']
                txtd3.insert(INSERT,'Package:'+' '+bq+'\n')
                txtd3.insert(INSERT,'Version:'+' '+Bw+'\n')
                txtd3.insert(INSERT,'Architecture:'+' '+be+'\n')  
                txtd3.insert(INSERT,'PreDepends:'+' ')  
                for frag1 in ba: 
                 if  "," in frag1 or  "|" in frag1:
                    txtd3.insert(INSERT, frag1)
                 else:
                    txtd3.insert(INSERT, frag1,"likes")
              else:         
                txtd3.insert(INSERT,'Package:'+' '+bq+'\n')
                txtd3.insert(INSERT,'Version:'+' '+Bw+'\n')
                txtd3.insert(INSERT,'Architecture:'+' '+be)   
            txtd3.insert(INSERT,'\n'+'\n')
            txtd3.tag_config("likes", foreground='#d2d2d2', underline=1) 
            txtd3.tag_bind("likes", "<1>",namepac1)
      else:
        Textdb=Textdb
        number1 = collection.count_documents({'Package': Textdb})
        if number1==0:
          txtd3.insert(INSERT,'Даного пакета нет в базе данных')
        else:  
          print('Ok')
        for channel in collection.find({'Package': Textdb}):
          bq=channel['Package']
          Bw=channel['Version']
          be=channel['Architecture']
          if 'Depends' in channel:
            br=channel['Depends']
            txtd3.insert(INSERT,'Package:'+' '+bq+'\n')
            txtd3.insert(INSERT,'Version:'+' '+Bw+'\n')
            txtd3.insert(INSERT,'Architecture:'+' '+be+'\n')
            txtd3.insert(INSERT,'Depends:'+' ')
            for frag in br: 
              if  "," in frag or  "|" in frag:
                txtd3.insert(INSERT, frag) 
              else:
                txtd3.insert(INSERT, frag,"likes")
            if 'PreDepends' in channel:
              ba=channel['PreDepends']
              txtd3.insert(INSERT,"\n"+'PreDepends:'+' ')  
              for frag1 in ba: 
                if  "," in frag1 or  "|" in frag1:
                  txtd3.insert(INSERT, frag1)
                else:
                  txtd3.insert(INSERT, frag1,"likes")  
          else: 
            if 'PreDepends' in channel:
              ba=channel['PreDepends']
              txtd3.insert(INSERT,'Package:'+' '+bq+'\n')
              txtd3.insert(INSERT,'Version:'+' '+Bw+'\n')
              txtd3.insert(INSERT,'Architecture:'+' '+be+'\n')  
              txtd3.insert(INSERT,'PreDepends:'+' ')  
              for frag1 in ba: 
                if  "," in frag1 or  "|" in frag1:
                  txtd3.insert(INSERT, frag1)
                else:
                  txtd3.insert(INSERT, frag1,"likes")
            else:         
              txtd3.insert(INSERT,'Package:'+' '+bq+'\n')
              txtd3.insert(INSERT,'Version:'+' '+Bw+'\n')
              txtd3.insert(INSERT,'Architecture:'+' '+be)   
          txtd3.insert(INSERT,'\n'+'\n')
          txtd3.tag_config("likes", foreground='#d2d2d2', underline=1) 
          txtd3.tag_bind("likes", "<1>",namepac1) 
    click_point = "@%s,%s" % (event.x, event.y)
    trs = txtd2.tag_ranges("likes")
    Textdb = ""
    # определяется, на какой участок пришелся щелчок мыши, и берется
    # соответствующий ему URL
    for i in range(0, len(trs), 1):
      if txtd2.compare(trs[i], "<=", click_point) and \
        txtd2.compare(click_point, "<=", trs[i+1]):
        Textdb = txtd2.get(trs[i], trs[i+1])
      # Prinr.delete("1.0", END)
        a,b = Textdb.split()
        a = a.replace(",",'')
    print(a)  
    print(b)
    root5 = Tk()
    root5.title('Поиск по пакетам')
    root5['bg'] ='#2c2c2c'
    root5.geometry('500x350')
    root5.resizable(width=False,height=False)
    Packagedepens_label=Label(root5,text=f"{a}, {b}",font=("Arial Bold", 15), bg='#2c2c2c',fg='#d2d2d2',padx=10,pady=8)
    Packagedepens_label.pack()
    txtd3 = scrolledtext.ScrolledText(root5,width=40,height=15,font=("Arial Bold", 10), bg='#2c2c2c',fg='#d2d2d2',padx=10,pady=8, cursor="hand2")
    txtd3.pack()
    number1 = collection.count_documents({'$and': [{'Package': a},{'Version': b}]})
    if number1==0:
      txtd3.insert(INSERT,'Даного пакета нет в базе данных')
    else:  
      print('Ok')
    for channel in collection.find({'$and': [{'Package': a},{'Version': b}]}):
     bq=channel['Package']
     Bw=channel['Version']
     be=channel['Architecture']
     if 'Depends' in channel:
      br=channel['Depends']
      txtd3.insert(INSERT,'Package:'+' '+bq+'\n')
      txtd3.insert(INSERT,'Version:'+' '+Bw+'\n')
      txtd3.insert(INSERT,'Architecture:'+' '+be+'\n')
      txtd3.insert(INSERT,'Depends:'+' ')
      for frag in br: 
       if  "," in frag or  "|" in frag:
        txtd3.insert(INSERT, frag) 
       else:
        txtd3.insert(INSERT, frag,"likes")
      if 'PreDepends' in channel:
        ba=channel['PreDepends']
        txtd3.insert(INSERT,"\n"+'PreDepends:'+' ')  
        for frag1 in ba: 
          if  "," in frag1 or  "|" in frag1:
           txtd3.insert(INSERT, frag1)
          else:
           txtd3.insert(INSERT, frag1,"likes")  
     else: 
       if 'PreDepends' in channel:
         ba=channel['PreDepends']
         txtd3.insert(INSERT,'Package:'+' '+bq+'\n')
         txtd3.insert(INSERT,'Version:'+' '+Bw+'\n')
         txtd3.insert(INSERT,'Architecture:'+' '+be+'\n')  
         txtd3.insert(INSERT,'PreDepends:'+' ')  
         for frag1 in ba: 
           if  "," in frag1 or  "|" in frag1:
            txtd3.insert(INSERT, frag1)
           else:
            txtd3.insert(INSERT, frag1,"likes")
       else:         
        txtd3.insert(INSERT,'Package:'+' '+bq+'\n')
        txtd3.insert(INSERT,'Version:'+' '+Bw+'\n')
        txtd3.insert(INSERT,'Architecture:'+' '+be)   
     txtd3.insert(INSERT,'\n'+'\n')
     txtd3.tag_config("likes", foreground='#d2d2d2', underline=1) 
     txtd3.tag_bind("likes", "<1>",namepac1)
    root5.mainloop()
 def dbinf2():
    # отчиска поля   
    txtd2.delete(1.0, END)
    # подключение к бд
    BDconect()
    Packagedepens= Packagedepens_entry.get()
    #вывод количества пакетов
    number1 = collection.count_documents({'Depends': {'$regex': Packagedepens}})
    if number1==0:  
      txtd2.insert(INSERT,'Даного пакета нет в базе данных')
    else:         
      txtd2.insert(INSERT,'количество пакетов  ')
      txtd2.insert(INSERT,number1)
      txtd2.insert(INSERT,'\n')
    #вывод пакетов
    for channel2 in collection.find({'Depends': {'$regex': Packagedepens}} ):
     # global fz
      zd=channel2['Package']
      dz=channel2['Version']
      fz=zd+', '+dz+'\n' 
      txtd2.insert(END, " ")
      txtd2.insert(END, fz ,"likes")
      txtd2.tag_config("likes", foreground='#d2d2d2') 
      txtd2.tag_bind("likes", "<1>",clu)
  # окно Поиск по зависимостям
 root4 = Tk()
 def btnReturn(e):
    dbinf2()
 def limitSizeDay(event):
   value = Packagedepens_entry.get()
   if len(value)>1:
     send3_btn.config(state='normal')
     root4.bind('<Return>', btnReturn)
   else:
     send3_btn.config(state='disabled')
 root4.title('Поиск по зависимости пакета')
 root4['bg'] ='#2c2c2c'
 root4.geometry('500x450')
 root4.resizable(width=False,height=False)
 Packagedepens_label=Label(root4,text='зависимость пакета',font=("Arial Bold", 10), bg='#2c2c2c',fg='#d2d2d2',padx=10,pady=8)
 Packagedepens_label.pack()
 Packagedepens_entry = Entry(root4,bg='white',fg='#2c2c2c', font=("Arial Bold", 10))
 Packagedepens_entry.pack()
 send3_btn= Button(root4,text="Найти",bg='#2c2c2c',fg='#d2d2d2',command = dbinf2)
 send3_btn.pack(padx=15,pady=10)
 txtd2 = scrolledtext.ScrolledText(root4,width=40,height=15,font=("Arial Bold", 10), bg='#2c2c2c',fg='#d2d2d2',padx=10,pady=8, cursor="hand2")
 txtd2.pack()
 
 root4.bind("<Enter>",  limitSizeDay)
 root4.mainloop()