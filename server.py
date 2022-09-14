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
# подключение к бд  
def btn_3clicked(): 
  def click():
    from pymongo import MongoClient
    global username # создание глобальной переменой
    global Password # создание глобальной переменой
    global Address # создание глобальной переменой
    username = username_entry.get() 
    Password = Password_entry.get()
    Address = Address_entry.get()  
    root2.destroy()
    # вывод окна о успешном подключении
    text = Address
    text = text.replace("user", username )
    text = text.replace("<password>", Password)
    print(text)
    try:
     cluster = MongoClient(text)
     try:
       print("MongoDB version is %s" %
               cluster.server_info()['version'])
       messagebox.showinfo('подключение успешно пройдено',f'{username},{Password},{Address}')
     except pymongo.errors.OperationFailure as error:
        messagebox.showerror("\nНет подключения к серверу","\nПроверьте введённые данные")
        btn_3clicked()           
    except pymongo.errors.InvalidURI:
        messagebox.showerror("\nНет подключения к серверу","\nПроверьте введённые данные")
        btn_3clicked()  
     # запись данных о авторизации
    with open("log.txt", "w",encoding='utf-8') as f:
     f.write(username+'\n'+Password+'\n'+Address)
    f.close 
    
  # окно авторизации
  root2 = Tk()
  def btnReturn2(e):
    click()
  root2.title('Авторизация')
  root2.geometry('450x230')
  root2.resizable(width=False,height=False)
  root2['bg']='#2c2c2c'
  username_label=Label(root2,text='Имя пользователя',font=("Arial Bold", 10), bg='#2c2c2c',fg='#d2d2d2',padx=10,pady=8)
  username_label.pack()
  username_entry = Entry(root2,bg='white',fg='#2c2c2c', font=("Arial Bold", 10))
  username_entry.pack()
  Password_label=Label(root2,text='Пароль',font=("Arial Bold", 10), bg='#2c2c2c',fg='#d2d2d2',padx=10,pady=8)
  Password_label.pack()
  Password_entry = Entry(root2,bg='white',fg='#2c2c2c', font=("Arial Bold", 10))
  Password_entry.pack()
  Address_label=Label(root2,text='Адрес',font=("Arial Bold", 10), bg='#2c2c2c',fg='#d2d2d2',padx=10,pady=8)
  Address_label.pack()
  Address_entry = Entry(root2,bg='white',fg='#2c2c2c', font=("Arial Bold", 10))
  Address_entry.pack()
  send_btn=Button(root2,text="Войти",bg='#2c2c2c',fg='#d2d2d2',command=click)
  send_btn.pack(padx=10,pady=8)
  
   # сохранение данных о авторизации
  with open("log.txt", "r") as f:
   sd = f.readline().split()
   sf = f.readline().split()
   sz = f.readline().split()
  f.close() 
  username_entry.insert(0,sd)
  Password_entry.insert(0,sf)
  Address_entry.insert(0, sz)
  root2.bind('<Return>', btnReturn2)
  root2.mainloop()