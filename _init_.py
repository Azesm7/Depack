# подключение к библеотекам
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
from tree_search import *
from search_by_Depends import *
from search_by_name2 import *
from server import *
#from Init import *
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
   #messagebox.showinfo("Ошибка","\nНет подключения к серверу. Проверьте введённые данные\n")
  else:
    messagebox.showerror("Ошибка","\nНет подключения к серверу. Откройте меню настройки и выберите пункт сервер и введите данные о сервере\n")
 except FileNotFoundError:
    messagebox.showerror("Ошибка","\nНет подключения к серверу. Откройте меню настройки и выберите пункт сервер и введите данные о сервере\n") 
name = ""
def btn_2clicked():  # открытие файла
  # создание глобальной переменой
  global name 
  name = tk.filedialog.askopenfilename() # открытие окна выбора файла 
  txtd5.insert(INSERT,name) # Отправка сообщения об открытии файла в главное окно
# авторизация...
 #Отправка в бд
def homea():
  global name  
  name=name.split("/")
  name= name.pop()
  name="/home/user/"+name 
def btn_clicked():
 try: 
  try:  
    try:  
     if name != "":
       faile = open(name,'r',encoding='utf-8') # редактирование файла
       lines = faile.readlines() # чтение строк
       faile.close
       faile = open(name + 's.json','w',encoding='utf-8') # записывание нужной информации
       for line in lines:
          if "Package:" in line:
            faile.write("},"+"\n"+"{"+"\n"+line)  
          elif "Version:" in line:
           faile.write(line)
          elif "Architecture:" in line:
            faile.write(line)
          elif "Depends:" in line:
            faile.write(line)
       faile.close()
   # добовление необходимых символов и исправление ошибок после записи
       str = 'Ghc-                                                                                                                                                                                                                                                                                                                                                                        Package:'
       pattern = re.compile(re.escape(str))
       with open(name + 's.json', 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            result = pattern.search(line)
            if result is None:
                f.write(line)
            f.truncate()
        str4 = 'Ghc-Package:'
       pattern = re.compile(re.escape(str4))
       with open(name + 's.json', 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            result = pattern.search(line)
            if result is None:
                f.write(line)
            f.truncate()  
        str2 = 'Auto-Built-Package:'
       pattern = re.compile(re.escape(str2))
       with open(name + 's.json', 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            result = pattern.search(line)
            if result is None:
                f.write(line)
            f.truncate()
       with open(name + 's.json','r+',encoding='utf-8') as f:
        lines = list(map(lambda x: '{}"\n'.format(x.strip()), f.readlines()))
        f.seek(0)
        [f.write(l) for l in lines]
       f.close()
       with open(name + 's.json','r+',encoding='utf-8') as f: 
        lines = list(map(lambda x: '{},\n'.format(x.strip()), f.readlines()))
        f.seek(0)
        [f.write(l) for l in lines]
       f.close()
       with open(name + 's.json', 'rb+') as filehandle:
        filehandle.seek(-2, os.SEEK_END)
        filehandle.truncate()
       filehandle.close()   
       with open(name + 's.json','a',encoding='utf-8') as f: 
        f.write('\n'+"}"+'\n'+"]")
       f.close()
       with open(name + 's.json',encoding='utf-8') as file_in:
        text = file_in.read()

       text = text.replace('},",', '},')

       with open(name + 's.json','w',encoding='utf-8') as file_out:
        file_out.write(text)
       faile.close()
       with open(name + 's.json',encoding='utf-8') as file_in:
        text = file_in.read()

       text = text.replace('{",', '{')

       with open(name + 's.json','w',encoding='utf-8') as file_out:
        file_out.write(text)
       faile.close()
       with open(name + 's.json',encoding='utf-8') as file_in:
        text = file_in.read()

       text = text.replace('Package: ', '"Package": "')

       with open(name + 's.json','w',encoding='utf-8') as file_out:
        file_out.write(text)
        faile.close()
       with open(name + 's.json',encoding='utf-8') as file_in:
        text = file_in.read()

       text = text.replace('Architecture: ', '"Architecture": "')

       with open(name + 's.json','w',encoding='utf-8') as file_out:
        file_out.write(text)
       faile.close()
       with open(name + 's.json',encoding='utf-8') as file_in:
        text = file_in.read()

       text = text.replace('Version: ', '"Version": "')

       with open(name + 's.json','w',encoding='utf-8') as file_out:
        file_out.write(text)
       faile.close()
       with open(name + 's.json',encoding='utf-8') as file_in:
        text = file_in.read()

       text = text.replace('Depends: ', '"Depends": "')

       with open(name + 's.json','w',encoding='utf-8') as file_out:
        file_out.write(text)
       faile.close()
       with open(name + 's.json',encoding='utf-8') as file_in:
        text = file_in.read()

       text = text.replace('",\n},', '"\n},')

       with open(name + 's.json','w',encoding='utf-8') as file_out:
        file_out.write(text)
       faile.close()
       with open(name + 's.json',encoding='utf-8') as file_in:
        text = file_in.read()

       text = text.replace('",\n Python-"Version": "', 'Python-Version: ')

       with open(name + 's.json','w',encoding='utf-8') as file_out:
        file_out.write(text)
       faile.close()
       with open(name + 's.json',encoding='utf-8') as file_in:
        text = file_in.read()

       text = text.replace('",\nPython-"Version": "', 'Python-Version: ')

       with open(name + 's.json','w',encoding='utf-8') as file_out:
        file_out.write(text)
       faile.close()
    
       text = text.replace('",\n Python3-"Version": "', 'Python3-Version: ')

       with open(name + 's.json','w',encoding='utf-8') as file_out:
        file_out.write(text)
       faile.close()
       with open(name + 's.json','w',encoding='utf-8') as file_out:
        file_out.write(text)
       faile.close()
       text = text.replace('},\n{\n},\n{', '},\n{')
    
       with open(name + 's.json','w',encoding='utf-8') as file_out:
        file_out.write(text)
       faile.close()
       with open(name + 's.json','w',encoding='utf-8') as file_out:
        file_out.write(text)
       faile.close()
       text = text.replace('Pre-"Depends"', '"PreDepends"')

       with open(name + 's.json','w',encoding='utf-8') as file_out:
        file_out.write(text)
       faile.close()
       with open(name + 's.json','w',encoding='utf-8') as file_out:
        file_out.write(text)
       faile.close()
       text = text.replace('",\nPython3-"Version": "', 'Python3-Version: ')

       with open(name + 's.json','w',encoding='utf-8') as file_out:
        file_out.write(text)
       faile.close()
       with open(name + 's.json','w',encoding='utf-8') as file_out:
        file_out.write(text)
       faile.close()
       text = text.replace('",\nGstreamer-"Version": "', 'Gstreamer-Version: ')

       with open(name + 's.json','w',encoding='utf-8') as file_out:
        file_out.write(text)
        faile.close()
       with open(name + 's.json','r+',encoding='utf-8') as f: 
        f.seek(0)
        f.write('[ ')
       f.close()
    # вывод об преобразование файла 
       txtd5.insert(INSERT,"\n"+'Преобразование файла в json завершено')
    #работа с бд
       with open(name + 's.json','r',encoding='utf-8') as f: # открытие файла
        templates = json.load(f) # считывание json файла
       BDconect() # Подключение к бд
       it_pylounge = templates # передача информации с файла переменой
       ins_result = collection.insert_many(it_pylounge).inserted_ids  # добавляет несколько записей в коллекцию collection
    # вывод сообщение об отпраки данных
       txtd5.insert(INSERT,"\n"+'Данные отправлены'+"\n") # вывод сообщения
       os.remove(name + 's.json')
     else:    
      messagebox.showerror("Ошибка","Файл не найден. Зайдите в настройки и выберите файл"+"\n")
    except PermissionError:
     if name != "":
       faile = open(name,'r',encoding='utf-8') # редактирование файла
       lines = faile.readlines() # чтение строк
       faile.close
       homea()
       faile = open(name + 's.json','w',encoding='utf-8') # записывание нужной информации
       for line in lines:
          if "Package:" in line:
            faile.write("},"+"\n"+"{"+"\n"+line)  
          elif "Version:" in line:
            faile.write(line)
          elif "Architecture:" in line:
            faile.write(line)
          elif "Depends:" in line:
            faile.write(line)
       faile.close()
   # добовление необходимых символов и исправление ошибок после записи
       str = 'Ghc-                                                                                                                                                                                                                                                                                                                                                                        Package:'
       pattern = re.compile(re.escape(str))
       with open(name + 's.json', 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            result = pattern.search(line)
            if result is None:
                f.write(line)
            f.truncate()
        str4 = 'Ghc-Package:'
       pattern = re.compile(re.escape(str4))
       with open(name + 's.json', 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            result = pattern.search(line)
            if result is None:
                f.write(line)
            f.truncate()  
        str2 = 'Auto-Built-Package:'
       pattern = re.compile(re.escape(str2))
       with open(name + 's.json', 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            result = pattern.search(line)
            if result is None:
                f.write(line)
            f.truncate()
       with open(name + 's.json','r+',encoding='utf-8') as f:
        lines = list(map(lambda x: '{}"\n'.format(x.strip()), f.readlines()))
        f.seek(0)
        [f.write(l) for l in lines]
       f.close()
       with open(name + 's.json','r+',encoding='utf-8') as f: 
        lines = list(map(lambda x: '{},\n'.format(x.strip()), f.readlines()))
        f.seek(0)
        [f.write(l) for l in lines]
       f.close()
       with open(name + 's.json', 'rb+') as filehandle:
        filehandle.seek(-2, os.SEEK_END)
        filehandle.truncate()
       filehandle.close()   
       with open(name + 's.json','a',encoding='utf-8') as f: 
        f.write('\n'+"}"+'\n'+"]")
       f.close()
       with open(name + 's.json',encoding='utf-8') as file_in:
        text = file_in.read()

       text = text.replace('},",', '},')
 
       with open(name + 's.json','w',encoding='utf-8') as file_out:
        file_out.write(text)
       faile.close()
       with open(name + 's.json',encoding='utf-8') as file_in:
        text = file_in.read()

       text = text.replace('{",', '{')

       with open(name + 's.json','w',encoding='utf-8') as file_out:
        file_out.write(text)
       faile.close()
       with open(name + 's.json',encoding='utf-8') as file_in:
        text = file_in.read()

       text = text.replace('Package: ', '"Package": "')

       with open(name + 's.json','w',encoding='utf-8') as file_out:
        file_out.write(text)
        faile.close()
       with open(name + 's.json',encoding='utf-8') as file_in:
        text = file_in.read()

       text = text.replace('Architecture: ', '"Architecture": "')

       with open(name + 's.json','w',encoding='utf-8') as file_out:
        file_out.write(text)
       faile.close()
       with open(name + 's.json',encoding='utf-8') as file_in:
        text = file_in.read()

       text = text.replace('Version: ', '"Version": "')

       with open(name + 's.json','w',encoding='utf-8') as file_out:
        file_out.write(text)
       faile.close()
       with open(name + 's.json',encoding='utf-8') as file_in:
        text = file_in.read()

       text = text.replace('Depends: ', '"Depends": "')

       with open(name + 's.json','w',encoding='utf-8') as file_out:
        file_out.write(text)
       faile.close()
       with open(name + 's.json',encoding='utf-8') as file_in:
        text = file_in.read()

       text = text.replace('",\n},', '"\n},')

       with open(name + 's.json','w',encoding='utf-8') as file_out:
        file_out.write(text)
       faile.close()
       with open(name + 's.json',encoding='utf-8') as file_in:
        text = file_in.read()

       text = text.replace('",\n Python-"Version": "', 'Python-Version: ')

       with open(name + 's.json','w',encoding='utf-8') as file_out:
        file_out.write(text)
       faile.close()
       with open(name + 's.json',encoding='utf-8') as file_in:
        text = file_in.read()

       text = text.replace('",\nPython-"Version": "', 'Python-Version: ')

       with open(name + 's.json','w',encoding='utf-8') as file_out:
        file_out.write(text)
       faile.close()
    
       text = text.replace('",\n Python3-"Version": "', 'Python3-Version: ')

       with open(name + 's.json','w',encoding='utf-8') as file_out:
        file_out.write(text)
       faile.close()
       with open(name + 's.json','w',encoding='utf-8') as file_out:
        file_out.write(text)
       faile.close()
       text = text.replace('},\n{\n},\n{', '},\n{')
    
       with open(name + 's.json','w',encoding='utf-8') as file_out:
        file_out.write(text)
       faile.close()
       with open(name + 's.json','w',encoding='utf-8') as file_out:
        file_out.write(text)
       faile.close()
       text = text.replace('Pre-"Depends"', '"PreDepends"')

       with open(name + 's.json','w',encoding='utf-8') as file_out:
        file_out.write(text)
       faile.close()
       with open(name + 's.json','w',encoding='utf-8') as file_out:
        file_out.write(text)
       faile.close()
       text = text.replace('",\nPython3-"Version": "', 'Python3-Version: ')

       with open(name + 's.json','w',encoding='utf-8') as file_out:
        file_out.write(text)
       faile.close()
       with open(name + 's.json','w',encoding='utf-8') as file_out:
        file_out.write(text)
       faile.close()
       text = text.replace('",\nGstreamer-"Version": "', 'Gstreamer-Version: ')

       with open(name + 's.json','w',encoding='utf-8') as file_out:
        file_out.write(text)
       faile.close()
       with open(name + 's.json','r+',encoding='utf-8') as f: 
        f.seek(0)
        f.write('[ ')
       f.close()
    # вывод об преобразование файла 
       txtd5.insert(INSERT,"\n"+'Преобразование файла в json завершено')
    #работа с бд
       with open(name + 's.json','r',encoding='utf-8') as f: # открытие файла
        templates = json.load(f) # считывание json файла
       BDconect() # Подключение к бд
       it_pylounge = templates # передача информации с файла переменой
       ins_result = collection.insert_many(it_pylounge).inserted_ids  # добавляет несколько записей в коллекцию collection
    # вывод сообщение об отпраки данных
       txtd5.insert(INSERT,"\n"+'Данные отправлены'+"\n") # вывод сообщения
       os.remove(name + 's.json')
     else:    
       messagebox.showerror("Ошибка","Файл не найден. Зайдите в настройки и выберите файл"+"\n")
  except UnboundLocalError: 
     messagebox.showerror("Ошибка","\n"+"Выберите другой файл,данный неправильного формата"+"\n")         
     os.remove(name + 's.json')
 except OSError:
     messagebox.showerror("Ошибка","\n"+"Выберите другой файл,данный неправильного формата"+"\n")
     os.remove(name + 's.json') 
root = Tk()
username = "" # создание глобальной переменой
Password = "" # создание глобальной переменой
Address = "" # создание глобальной переменой
# главное окно   
root['bg'] ='#2c2c2c' 
root.title("depack")
root.geometry('500x450')
root.resizable(width=False,height=False)
# создание меню
from tkinter import Menu
menu = Menu(root)
menu['bg'] ='#181818' 
menu['fg'] ='#d2d2d2'
new_item = Menu(menu) 
new_item = Menu(menu, tearoff=0)
new_item['bg'] ='#181818' 
new_item['fg'] ='#d2d2d2'
new_item.add_command(label='Init',command=btn_clicked)  
menu.add_cascade(label='Fite', menu=new_item)  
new_item = Menu(menu) 
new_item = Menu(menu, tearoff=0)
new_item['bg'] ='#181818' 
new_item['fg'] ='#d2d2d2' 
new_item.add_command(label='файл',command=btn_2clicked)
new_item.add_command(label='Сервер',command=btn_3clicked)    
menu.add_cascade(label='Настройки', menu=new_item) 
new_item = Menu(menu)  
new_item = Menu(menu, tearoff=0)
new_item['bg'] ='#181818' 
new_item['fg'] ='#d2d2d2'
new_item.add_command(label='Поиск по имени пакета',command=btn_bd)
new_item.add_command(label='Поиск по завистимости пакета',command=btn_bd2)
new_item.add_command(label='Поиск дерева зависимости пакета',command=btn_bd7)      
menu.add_cascade(label='Операции', menu=new_item) 
root.config(menu=menu)  
txtd5 = scrolledtext.ScrolledText(root,width=51,height=25,font=("Arial Bold", 10), bg='#2c2c2c',fg='#d2d2d2',padx=10,pady=15, cursor="hand2")
txtd5.pack()
root.mainloop()
