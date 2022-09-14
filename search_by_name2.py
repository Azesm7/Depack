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
def btn_bd(): #поиск по имени пакета
 def namepac(event):
    def namepac1(event):
      click_point = "@%s,%s" % (event.x, event.y)
      trs = txtd4.tag_ranges("likes")
      Textdb = ""
      # определяется, на какой участок пришелся щелчок мыши, и берется
      # соответствующий ему URL
      for i in range(0, len(trs), 1):
        if txtd4.compare(trs[i], "<=", click_point) and \
          txtd4.compare(click_point, "<=", trs[i+1]):
          Textdb = txtd4.get(trs[i], trs[i+1])
      # Prinr.delete("1.0", END)
      print(Textdb)
      txtd4.delete(1.0, END)
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
            txtd4.insert(INSERT,'Даного пакета нет в базе данных')
          else:  
            print('Ok') 
          for channel in collection.find({'Package': {'$regex': a}}):
            bq=channel['Package']
            Bw=channel['Version']
            be=channel['Architecture']
            if 'Depends' in channel:
              br=channel['Depends']
              txtd4.insert(INSERT,'Package:'+' '+bq+'\n')
              txtd4.insert(INSERT,'Version:'+' '+Bw+'\n')
              txtd4.insert(INSERT,'Architecture:'+' '+be+'\n')
              txtd4.insert(INSERT,'Depends:'+' ')
              for frag in br: 
                if  "," in frag or  "|" in frag:
                  txtd4.insert(INSERT, frag) 
                else:
                  txtd4.insert(INSERT, frag,"likes")
              if 'PreDepends' in channel:
                ba=channel['PreDepends']
                txtd4.insert(INSERT,"\n"+'PreDepends:'+' ')  
                for frag1 in ba: 
                  if  "," in frag1 or  "|" in frag1:
                    txtd4.insert(INSERT, frag1)
                  else:
                    txtd4.insert(INSERT, frag1,"likes")  
            else: 
              if 'PreDepends' in channel:
                ba=channel['PreDepends']
                txtd4.insert(INSERT,'Package:'+' '+bq+'\n')
                txtd4.insert(INSERT,'Version:'+' '+Bw+'\n')
                txtd4.insert(INSERT,'Architecture:'+' '+be+'\n')  
                txtd4.insert(INSERT,'PreDepends:'+' ')  
                for frag1 in ba: 
                  if  "," in frag1 or  "|" in frag1:
                    txtd4.insert(INSERT, frag1)
                  else:
                    txtd4.insert(INSERT, frag1,"likes")  
              else:         
                txtd4.insert(INSERT,'Package:'+' '+bq+'\n')
                txtd4.insert(INSERT,'Version:'+' '+Bw+'\n')
                txtd4.insert(INSERT,'Architecture:'+' '+be)   
            txtd4.insert(INSERT,'\n'+'\n')
            txtd4.tag_config("likes", foreground='#d2d2d2', underline=1) 
          txtd4.tag_bind("likes", "<1>",namepac1)
        else:  
          a,b=Textdb.split()
          print(Textdb)
          print(a)
          print(b)
          number1 = collection.count_documents({'$and': [{'Package': a},{'Version': b}]})
          if number1==0:
            txtd4.insert(INSERT,'Даного пакета нет в базе данных')
          else:  
            print('Ok') 
          for channel in collection.find({'$and': [{'Package': a},{'Version': b}]}):
            bq=channel['Package']
            Bw=channel['Version']
            be=channel['Architecture']
            if 'Depends' in channel:
              br=channel['Depends']
              txtd4.insert(INSERT,'Package:'+' '+bq+'\n')
              txtd4.insert(INSERT,'Version:'+' '+Bw+'\n')
              txtd4.insert(INSERT,'Architecture:'+' '+be+'\n')
              txtd4.insert(INSERT,'Depends:'+' ')
              for frag in br: 
                if  "," in frag or  "|" in frag:
                  txtd4.insert(INSERT, frag) 
                else:
                  txtd4.insert(INSERT, frag,"likes")
              if 'PreDepends' in channel:
                ba=channel['PreDepends']
                txtd4.insert(INSERT,"\n"+'PreDepends:'+' ')  
                for frag1 in ba: 
                  if  "," in frag1 or  "|" in frag1:
                    txtd4.insert(INSERT, frag1)
                  else:
                    txtd4.insert(INSERT, frag1,"likes")  
            else: 
              if 'PreDepends' in channel:
                ba=channel['PreDepends']
                txtd4.insert(INSERT,'Package:'+' '+bq+'\n')
                txtd4.insert(INSERT,'Version:'+' '+Bw+'\n')
                txtd4.insert(INSERT,'Architecture:'+' '+be+'\n')  
                txtd4.insert(INSERT,'PreDepends:'+' ')  
                for frag1 in ba: 
                 if  "," in frag1 or  "|" in frag1:
                    txtd4.insert(INSERT, frag1)
                 else:
                    txtd4.insert(INSERT, frag1,"likes")
              else:         
                txtd4.insert(INSERT,'Package:'+' '+bq+'\n')
                txtd4.insert(INSERT,'Version:'+' '+Bw+'\n')
                txtd4.insert(INSERT,'Architecture:'+' '+be)   
            txtd4.insert(INSERT,'\n'+'\n')
            txtd4.tag_config("likes", foreground='#d2d2d2', underline=1) 
            txtd4.tag_bind("likes", "<1>",namepac1)
      else:
        Textdb=Textdb
        number1 = collection.count_documents({'Package': Textdb})
        if number1==0:
          txtd4.insert(INSERT,'Даного пакета нет в базе данных')
        else:  
          print('Ok') 
        for channel in collection.find({'Package': Textdb}):
          bq=channel['Package']
          Bw=channel['Version']
          be=channel['Architecture']
          if 'Depends' in channel:
            br=channel['Depends']
            txtd4.insert(INSERT,'Package:'+' '+bq+'\n')
            txtd4.insert(INSERT,'Version:'+' '+Bw+'\n')
            txtd4.insert(INSERT,'Architecture:'+' '+be+'\n')
            txtd4.insert(INSERT,'Depends:'+' ')
            for frag in br: 
              if  "," in frag or  "|" in frag:
                txtd4.insert(INSERT, frag) 
              else:
                txtd4.insert(INSERT, frag,"likes")
            if 'PreDepends' in channel:
              ba=channel['PreDepends']
              txtd4.insert(INSERT,"\n"+'PreDepends:'+' ')  
              for frag1 in ba: 
                if  "," in frag1 or  "|" in frag1:
                  txtd4.insert(INSERT, frag1)
                else:
                  txtd4.insert(INSERT, frag1,"likes")  
          else: 
            if 'PreDepends' in channel:
              ba=channel['PreDepends']
              txtd4.insert(INSERT,'Package:'+' '+bq+'\n')
              txtd4.insert(INSERT,'Version:'+' '+Bw+'\n')
              txtd4.insert(INSERT,'Architecture:'+' '+be+'\n')  
              txtd4.insert(INSERT,'PreDepends:'+' ')  
              for frag1 in ba: 
                if  "," in frag1 or  "|" in frag1:
                  txtd4.insert(INSERT, frag1)
                else:
                  txtd4.insert(INSERT, frag1,"likes")
            else:         
              txtd4.insert(INSERT,'Package:'+' '+bq+'\n')
              txtd4.insert(INSERT,'Version:'+' '+Bw+'\n')
              txtd4.insert(INSERT,'Architecture:'+' '+be)   
          txtd4.insert(INSERT,'\n'+'\n')
          txtd4.tag_config("likes", foreground='#d2d2d2', underline=1) 
          txtd4.tag_bind("likes", "<1>",namepac1) 
  #-------- 
    click_point = "@%s,%s" % (event.x, event.y)
    trs = txtd.tag_ranges("likes")
    Textdb = ""
    # определяется, на какой участок пришелся щелчок мыши, и берется
    # соответствующий ему URL
    for i in range(0, len(trs), 1):
      if txtd.compare(trs[i], "<=", click_point) and \
        txtd.compare(click_point, "<=", trs[i+1]):
        Textdb = txtd.get(trs[i], trs[i+1])
      # Prinr.delete("1.0", END)
    print(Textdb)
    root6 = Tk()
    root6.title('Поиск по зависимостям пакетов')
    root6['bg'] ='#2c2c2c'
    root6.geometry('500x350')
    root6.resizable(width=False,height=False)
    Packagedepens_label=Label(root6,text=Textdb,font=("Arial Bold", 15), bg='#2c2c2c',fg='#d2d2d2',padx=10,pady=8)
    Packagedepens_label.pack()
    txtd4 = scrolledtext.ScrolledText(root6,width=40,height=15,font=("Arial Bold", 10), bg='#2c2c2c',fg='#d2d2d2',padx=10,pady=8, cursor="hand2")
    txtd4.pack()
    Textdb = Textdb.replace(" ",'')
    Textdb = Textdb.replace("(",' ')
    Textdb = Textdb.replace("=",'')
    Textdb = Textdb.replace(")",'')
    if  " " in Textdb:
     if  "<" in Textdb or  ">" in Textdb:
      Textdb = Textdb.replace("<",'')
      Textdb = Textdb.replace(">",'')
      a,b=Textdb.split()
      a = a.replace(" ",'')
      number1 = collection.count_documents({'Package': {'$regex': a}})
      if number1==0:
         txtd4.insert(INSERT,'Даного пакета нет в базе данных')
      else:  
        print('Ok') 
      for channel in collection.find({'Package': {'$regex': a}}):
        bq=channel['Package']
        Bw=channel['Version']
        be=channel['Architecture']
        if 'Depends' in channel:
          br=channel['Depends']
          txtd4.insert(INSERT,'Package:'+' '+bq+'\n')
          txtd4.insert(INSERT,'Version:'+' '+Bw+'\n')
          txtd4.insert(INSERT,'Architecture:'+' '+be+'\n')
          txtd4.insert(INSERT,'Depends:'+' ')
          for frag in br: 
            if  "," in frag or  "|" in frag:
              txtd4.insert(INSERT, frag) 
            else:
              txtd4.insert(INSERT, frag,"likes")
          if 'PreDepends' in channel:
            ba=channel['PreDepends']
            txtd4.insert(INSERT,"\n"+'PreDepends:'+' ')  
            for frag1 in ba: 
              if  "," in frag1 or  "|" in frag1:
                txtd4.insert(INSERT, frag1)
              else:
                txtd4.insert(INSERT, frag1,"likes")  
        else: 
          if 'PreDepends' in channel:
            ba=channel['PreDepends']
            txtd4.insert(INSERT,'Package:'+' '+bq+'\n')
            txtd4.insert(INSERT,'Version:'+' '+Bw+'\n')
            txtd4.insert(INSERT,'Architecture:'+' '+be+'\n')  
            txtd4.insert(INSERT,'PreDepends:'+' ')  
            for frag1 in ba: 
              if  "," in frag1 or  "|" in frag1:
                txtd4.insert(INSERT, frag1)
              else:
                txtd4.insert(INSERT, frag1,"likes")
          else:         
            txtd4.insert(INSERT,'Package:'+' '+bq+'\n')
            txtd4.insert(INSERT,'Version:'+' '+Bw+'\n')
            txtd4.insert(INSERT,'Architecture:'+' '+be)   
        txtd4.insert(INSERT,'\n'+'\n')
        txtd4.tag_config("likes", foreground='#d2d2d2', underline=1) 
        txtd4.tag_bind("likes", "<1>",namepac1)
     else:  
      a,b=Textdb.split()
      print(Textdb)
      print(a)
      print(b)
      number1 = collection.count_documents({'$and': [{'Package': a},{'Version': b}]})
      if number1==0:
         txtd4.insert(INSERT,'Даного пакета нет в базе данных')
      else:  
        print('Ok') 
      for channel in collection.find({'$and': [{'Package': a},{'Version': b}]}):
        bq=channel['Package']
        Bw=channel['Version']
        be=channel['Architecture']
        if 'Depends' in channel:
          br=channel['Depends']
          txtd4.insert(INSERT,'Package:'+' '+bq+'\n')
          txtd4.insert(INSERT,'Version:'+' '+Bw+'\n')
          txtd4.insert(INSERT,'Architecture:'+' '+be+'\n')
          txtd4.insert(INSERT,'Depends:'+' ')
          for frag in br: 
            if  "," in frag or  "|" in frag:
              txtd4.insert(INSERT, frag) 
            else:
              txtd4.insert(INSERT, frag,"likes")
          if 'PreDepends' in channel:
            ba=channel['PreDepends']
            txtd4.insert(INSERT,"\n"+'PreDepends:'+' ')  
            for frag1 in ba: 
              if  "," in frag1 or  "|" in frag1:
                txtd4.insert(INSERT, frag1)
              else:
                txtd4.insert(INSERT, frag1,"likes")  
        else: 
          if 'PreDepends' in channel:
            ba=channel['PreDepends']
            txtd4.insert(INSERT,'Package:'+' '+bq+'\n')
            txtd4.insert(INSERT,'Version:'+' '+Bw+'\n')
            txtd4.insert(INSERT,'Architecture:'+' '+be+'\n')  
            txtd4.insert(INSERT,'PreDepends:'+' ')  
            for frag1 in ba: 
              if  "," in frag1 or  "|" in frag1:
                txtd4.insert(INSERT, frag1)
              else:
                txtd4.insert(INSERT, frag1,"likes")
          else:         
            txtd4.insert(INSERT,'Package:'+' '+bq+'\n')
            txtd4.insert(INSERT,'Version:'+' '+Bw+'\n')
            txtd4.insert(INSERT,'Architecture:'+' '+be)   
        txtd4.insert(INSERT,'\n'+'\n')
        txtd4.tag_config("likes", foreground='#d2d2d2', underline=1) 
        txtd4.tag_bind("likes", "<1>",namepac1)
    else:
      Textdb=Textdb
      Textdb = Textdb.replace(" ",'')
      number1 = collection.count_documents({'Package': Textdb})
      if number1==0:
         txtd4.insert(INSERT,'Даного пакета нет в базе данных')
      else:  
        print('Ok') 
      for channel in collection.find({'Package': Textdb}):
        bq=channel['Package']
        Bw=channel['Version']
        be=channel['Architecture']
        if 'Depends' in channel:
          br=channel['Depends']
          txtd4.insert(INSERT,'Package:'+' '+bq+'\n')
          txtd4.insert(INSERT,'Version:'+' '+Bw+'\n')
          txtd4.insert(INSERT,'Architecture:'+' '+be+'\n')
          txtd4.insert(INSERT,'Depends:'+' ')
          for frag in br: 
            if  "," in frag or  "|" in frag:
              txtd4.insert(INSERT, frag) 
            else:
              txtd4.insert(INSERT, frag,"likes")
          if 'PreDepends' in channel:
            ba=channel['PreDepends']
            txtd4.insert(INSERT,"\n"+'PreDepends:'+' ')  
            for frag1 in ba: 
              if  "," in frag1 or  "|" in frag1:
                txtd4.insert(INSERT, frag1)
              else:
                txtd4.insert(INSERT, frag1,"likes")  
        else: 
          if 'PreDepends' in channel:
            ba=channel['PreDepends']
            txtd4.insert(INSERT,'Package:'+' '+bq+'\n')
            txtd4.insert(INSERT,'Version:'+' '+Bw+'\n')
            txtd4.insert(INSERT,'Architecture:'+' '+be+'\n')  
            txtd4.insert(INSERT,'PreDepends:'+' ')  
            for frag1 in ba: 
              if  "," in frag1 or  "|" in frag1:
                txtd4.insert(INSERT, frag1)
              else:
                txtd4.insert(INSERT, frag1,"likes")
          else:         
            txtd4.insert(INSERT,'Package:'+' '+bq+'\n')
            txtd4.insert(INSERT,'Version:'+' '+Bw+'\n')
            txtd4.insert(INSERT,'Architecture:'+' '+be)     
        txtd4.insert(INSERT,'\n'+'\n')
        txtd4.tag_config("likes", foreground='#d2d2d2', underline=1) 
        txtd4.tag_bind("likes", "<1>",namepac1)
    root6.mainloop()  
 def dbinf():
    # отчиска поля   
    txtd.delete(1.0, END)
    # подключение к бд
    BDconect()
    #вывод количества пакетов
    PackageName= PackageName_entry.get()
    number1 = collection.count_documents({'Package': {'$regex': PackageName}})
    if number1==0:
       txtd.insert(INSERT,'Даного пакета нет в базе данных')
    else:   
     txtd.insert(INSERT,'Количество пакетов  ')
     txtd.insert(INSERT,number1)
     txtd.insert(INSERT,'\n'+'\n')
    # вывод информации о пакетов
    for channel in collection.find({'Package': {'$regex': PackageName}}):
     bq=channel['Package']
     Bw=channel['Version']
     be=channel['Architecture']
     if 'Depends' in channel:
      br=channel['Depends']
      txtd.insert(INSERT,'Package:'+' '+bq+'\n')
      txtd.insert(INSERT,'Version:'+' '+Bw+'\n')
      txtd.insert(INSERT,'Architecture:'+' '+be+'\n')
      txtd.insert(INSERT,'Depends:'+' ')
      for frag in br: 
       if  "," in frag or  "|" in frag:
        txtd.insert(INSERT, frag) 
       else:
        txtd.insert(INSERT, frag,"likes")
      if 'PreDepends' in channel:
        ba=channel['PreDepends']
        txtd.insert(INSERT,"\n"+'PreDepends:'+' ')  
        for frag1 in ba: 
          if  "," in frag1 or  "|" in frag1:
           txtd.insert(INSERT, frag1)
          else:
           txtd.insert(INSERT, frag1,"likes")  
     else: 
       if 'PreDepends' in channel:
         ba=channel['PreDepends']
         txtd.insert(INSERT,'Package:'+' '+bq+'\n')
         txtd.insert(INSERT,'Version:'+' '+Bw+'\n')
         txtd.insert(INSERT,'Architecture:'+' '+be+'\n')  
         txtd.insert(INSERT,'PreDepends:'+' ')  
         for frag1 in ba: 
           if  "," in frag1 or  "|" in frag1:
            txtd.insert(INSERT, frag1)
           else:
            txtd.insert(INSERT, frag1,"likes")
       else:         
        txtd.insert(INSERT,'Package:'+' '+bq+'\n')
        txtd.insert(INSERT,'Version:'+' '+Bw+'\n')
        txtd.insert(INSERT,'Architecture:'+' '+be)   
     txtd.insert(INSERT,'\n'+'\n')
     txtd.tag_config("likes", foreground='#d2d2d2', underline=1) 
     txtd.tag_bind("likes", "<1>",namepac)
 
 def btnReturn(e):
    dbinf()
    # окно поиск по имени пакета
 def limitSizeDay(event):
    value = PackageName_entry.get()
    if len(value)>1:
      send2_btn.config(state='normal')
      root3.bind('<Return>', btnReturn)
    else:
      send2_btn.config(state='disabled')
     
 root3 = Tk()
 root3.title('Поиск по имени пакета')
 root3['bg'] ='#2c2c2c'
 root3.geometry('500x450')
 root3.resizable(width=False,height=False)
 PackageName_label=Label(root3,text='Имя пакета',font=("Arial Bold", 10), bg='#2c2c2c',fg='#d2d2d2',padx=10,pady=8)
 PackageName_label.pack()
 PackageName_entry = Entry(root3,bg='white',fg='#2c2c2c', font=("Arial Bold", 10))
 PackageName_entry.pack()
 send2_btn= Button(root3,text="Найти",bg='#2c2c2c',fg='#d2d2d2',command = dbinf)
 send2_btn.pack(padx=15,pady=10)
 txtd = scrolledtext.ScrolledText(root3,width=40,height=15,font=("Arial Bold", 10), bg='#2c2c2c',fg='#d2d2d2',padx=10,pady=8)
 txtd.pack()
 root3.bind("<Enter>",  limitSizeDay)
 root3.mainloop()