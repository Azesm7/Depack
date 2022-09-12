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
# работа с файлом
#f = open("log.txt", "w")
#f.close  
root = Tk()
name = ""
username = "" # создание глобальной переменой
Password = "" # создание глобальной переменой
Address = "" # создание глобальной переменой
# подключение к бд
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
    #txtd5.insert(INSERT,"\nНет подключения к серверу. Проверьте введённые данные\n")
  else:
    txtd5.insert(INSERT,"\nНет подключения к серверу. Откройте меню настройки и выберите пункт сервер и введите данные о сервере\n")
 except FileNotFoundError:
    txtd5.insert(INSERT,"\nНет подключения к серверу. Откройте меню настройки и выберите пункт сервер и введите данные о сервере\n")   
  
  
def btn_bd7():
  BDconect()
  def namepac7(event):
      def namepac8(event):
        click_point = "@%s,%s" % (event.x, event.y)
        trs = txtd8.tag_ranges("likes")
        Textdb = ""
        # определяется, на какой участок пришелся щелчок мыши, и берется
        # соответствующий ему URL
        for i in range(0, len(trs), 1):
          if txtd8.compare(trs[i], "<=", click_point) and \
            txtd8.compare(click_point, "<=", trs[i+1]):
            Textdb = txtd8.get(trs[i], trs[i+1])
        # Prinr.delete("1.0", END)
        print(Textdb)
        txtd8.delete(1.0, END)
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
              txtd8.insert(INSERT,'Даного пакета нет в базе данных')
            else:  
              print('Ok') 
            for channel in collection.find({'Package': {'$regex': a}}):
              bq=channel['Package']
              Bw=channel['Version']
              be=channel['Architecture']
              if 'Depends' in channel:
                br=channel['Depends']
                txtd8.insert(INSERT,'Package:'+' '+bq+'\n')
                txtd8.insert(INSERT,'Version:'+' '+Bw+'\n')
                txtd8.insert(INSERT,'Architecture:'+' '+be+'\n')
                txtd8.insert(INSERT,'Depends:'+' ')
                for frag in br: 
                  if  "," in frag or  "|" in frag:
                    txtd8.insert(INSERT, frag) 
                  else:
                    txtd8.insert(INSERT, frag,"likes")
                if 'PreDepends' in channel:
                  ba=channel['PreDepends']
                  txtd8.insert(INSERT,"\n"+'PreDepends:'+' ')  
                  for frag1 in ba: 
                    if  "," in frag1 or  "|" in frag1:
                      txtd8.insert(INSERT, frag1)
                    else:
                      txtd8.insert(INSERT, frag1,"likes")  
              else: 
                if 'PreDepends' in channel:
                  ba=channel['PreDepends']
                  txtd8.insert(INSERT,'Package:'+' '+bq+'\n')
                  txtd8.insert(INSERT,'Version:'+' '+Bw+'\n')
                  txtd8.insert(INSERT,'Architecture:'+' '+be+'\n')  
                  txtd8.insert(INSERT,'PreDepends:'+' ')  
                  for frag1 in ba: 
                    if  "," in frag1 or  "|" in frag1:
                      txtd8.insert(INSERT, frag1)
                    else:
                      txtd8.insert(INSERT, frag1,"likes")  
                else:         
                  txtd8.insert(INSERT,'Package:'+' '+bq+'\n')
                  txtd8.insert(INSERT,'Version:'+' '+Bw+'\n')
                  txtd8.insert(INSERT,'Architecture:'+' '+be)   
              txtd8.insert(INSERT,'\n'+'\n')
              txtd8.tag_config("likes", foreground='#d2d2d2', underline=1) 
            txtd8.tag_bind("likes", "<1>",namepac8)
          else:  
            a,b=Textdb.split()
            print(Textdb)
            print(a)
            print(b)
            number1 = collection.count_documents({'$and': [{'Package': a},{'Version': b}]})
            if number1==0:
              txtd8.insert(INSERT,'Даного пакета нет в базе данных')
            else:  
              print('Ok') 
            for channel in collection.find({'$and': [{'Package': a},{'Version': b}]}):
              bq=channel['Package']
              Bw=channel['Version']
              be=channel['Architecture']
              if 'Depends' in channel:
                br=channel['Depends']
                txtd8.insert(INSERT,'Package:'+' '+bq+'\n')
                txtd8.insert(INSERT,'Version:'+' '+Bw+'\n')
                txtd8.insert(INSERT,'Architecture:'+' '+be+'\n')
                txtd8.insert(INSERT,'Depends:'+' ')
                for frag in br: 
                  if  "," in frag or  "|" in frag:
                   txtd8.insert(INSERT, frag) 
                  else:
                    txtd8.insert(INSERT, frag,"likes")
                if 'PreDepends' in channel:
                  ba=channel['PreDepends']
                  txtd8.insert(INSERT,"\n"+'PreDepends:'+' ')  
                  for frag1 in ba: 
                    if  "," in frag1 or  "|" in frag1:
                     txtd8.insert(INSERT, frag1)
                    else:
                      txtd8.insert(INSERT, frag1,"likes")  
              else: 
                if 'PreDepends' in channel:
                  ba=channel['PreDepends']
                  txtd8.insert(INSERT,'Package:'+' '+bq+'\n')
                  txtd8.insert(INSERT,'Version:'+' '+Bw+'\n')
                  txtd8.insert(INSERT,'Architecture:'+' '+be+'\n')  
                  txtd8.insert(INSERT,'PreDepends:'+' ')  
                  for frag1 in ba: 
                   if  "," in frag1 or  "|" in frag1:
                      txtd8.insert(INSERT, frag1)
                   else:
                      txtd8.insert(INSERT, frag1,"likes")
                else:         
                  txtd8.insert(INSERT,'Package:'+' '+bq+'\n')
                  txtd8.insert(INSERT,'Version:'+' '+Bw+'\n')
                  txtd8.insert(INSERT,'Architecture:'+' '+be)   
              txtd8.insert(INSERT,'\n'+'\n')
              txtd8.tag_config("likes", foreground='#d2d2d2', underline=1) 
              txtd8.tag_bind("likes", "<1>",namepac8)
        else:
          Textdb=Textdb
          number1 = collection.count_documents({'Package': Textdb})
          if number1==0:
            txtd8.insert(INSERT,'Даного пакета нет в базе данных')
          else:  
            print('Ok') 
          for channel in collection.find({'Package': Textdb}):
            bq=channel['Package']
            Bw=channel['Version']
            be=channel['Architecture']
            if 'Depends' in channel:
              br=channel['Depends']
              txtd8.insert(INSERT,'Package:'+' '+bq+'\n')
              txtd8.insert(INSERT,'Version:'+' '+Bw+'\n')
              txtd8.insert(INSERT,'Architecture:'+' '+be+'\n')
              txtd8.insert(INSERT,'Depends:'+' ')
              for frag in br: 
                if  "," in frag or  "|" in frag:
                  txtd8.insert(INSERT, frag) 
                else:
                  txtd8.insert(INSERT, frag,"likes")
              if 'PreDepends' in channel:
                ba=channel['PreDepends']
                txtd8.insert(INSERT,"\n"+'PreDepends:'+' ')  
                for frag1 in ba: 
                  if  "," in frag1 or  "|" in frag1:
                    txtd8.insert(INSERT, frag1)
                  else:
                    txtd8.insert(INSERT, frag1,"likes")  
            else: 
              if 'PreDepends' in channel:
                ba=channel['PreDepends']
                txtd8.insert(INSERT,'Package:'+' '+bq+'\n')
                txtd8.insert(INSERT,'Version:'+' '+Bw+'\n')
                txtd8.insert(INSERT,'Architecture:'+' '+be+'\n')  
                txtd8.insert(INSERT,'PreDepends:'+' ')  
                for frag1 in ba: 
                  if  "," in frag1 or  "|" in frag1:
                    txtd8.insert(INSERT, frag1)
                  else:
                    txtd8.insert(INSERT, frag1,"likes")
              else:         
                txtd8.insert(INSERT,'Package:'+' '+bq+'\n')
                txtd8.insert(INSERT,'Version:'+' '+Bw+'\n')
                txtd8.insert(INSERT,'Architecture:'+' '+be)   
            txtd8.insert(INSERT,'\n'+'\n')
            txtd8.tag_config("likes", foreground='#d2d2d2', underline=1) 
            txtd8.tag_bind("likes", "<1>",namepac8) 
  #-------- 
      click_point = "@%s,%s" % (event.x, event.y)
      trs = txtd7.tag_ranges("likes")
      Textdb = ""
      # определяется, на какой участок пришелся щелчок мыши, и берется
      # соответствующий ему URL
      for i in range(0, len(trs), 1):
        if txtd7.compare(trs[i], "<=", click_point) and \
          txtd7.compare(click_point, "<=", trs[i+1]):
          Textdb = txtd7.get(trs[i], trs[i+1])
      # Prinr.delete("1.0", END)
      print(Textdb)
      root8 = Tk()
      root8.title('Поиск по зависимостям пакетов')
      root8['bg'] ='#2c2c2c'
      root8.geometry('500x350')
      root8.resizable(width=False,height=False)
      Packagedepens_label=Label(root8,text=Textdb,font=("Arial Bold", 15), bg='#2c2c2c',fg='#d2d2d2',padx=10,pady=8)
      Packagedepens_label.pack()
      txtd8 = scrolledtext.ScrolledText(root8,width=40,height=15,font=("Arial Bold", 10), bg='#2c2c2c',fg='#d2d2d2',padx=10,pady=8, cursor="hand2")
      txtd8.pack()
      Textdb=Textdb
      number1 = collection.count_documents({'Package': Textdb})
      if number1==0:
        txtd8.insert(INSERT,'Даного пакета нет в базе данных')
      else:  
         print('Ok') 
      for channel in collection.find({'Package': Textdb}):
          bq=channel['Package']
          Bw=channel['Version']
          be=channel['Architecture']
          if 'Depends' in channel:
            br=channel['Depends']
            txtd8.insert(INSERT,'Package:'+' '+bq+'\n')
            txtd8.insert(INSERT,'Version:'+' '+Bw+'\n')
            txtd8.insert(INSERT,'Architecture:'+' '+be+'\n')
            txtd8.insert(INSERT,'Depends:'+' ')
            for frag in br: 
              if  "," in frag or  "|" in frag:
                txtd8.insert(INSERT, frag) 
              else:
                txtd8.insert(INSERT, frag,"likes")
            if 'PreDepends' in channel:
              ba=channel['PreDepends']
              txtd8.insert(INSERT,"\n"+'PreDepends:'+' ')  
              for frag1 in ba: 
                if  "," in frag1 or  "|" in frag1:
                  txtd8.insert(INSERT, frag1)
                else:
                  txtd8.insert(INSERT, frag1,"likes")  
          else: 
            if 'PreDepends' in channel:
              ba=channel['PreDepends']
              txtd8.insert(INSERT,'Package:'+' '+bq+'\n')
              txtd8.insert(INSERT,'Version:'+' '+Bw+'\n')
              txtd8.insert(INSERT,'Architecture:'+' '+be+'\n')  
              txtd8.insert(INSERT,'PreDepends:'+' ')  
              for frag1 in ba: 
                if  "," in frag1 or  "|" in frag1:
                  txtd8.insert(INSERT, frag1)
                else:
                  txtd8.insert(INSERT, frag1,"likes")
            else:         
              txtd8.insert(INSERT,'Package:'+' '+bq+'\n')
              txtd8.insert(INSERT,'Version:'+' '+Bw+'\n')
              txtd8.insert(INSERT,'Architecture:'+' '+be)     
          txtd8.insert(INSERT,'\n'+'\n')
          txtd8.tag_config("likes", foreground='#d2d2d2', underline=1) 
          txtd8.tag_bind("likes", "<1>",namepac8)
      root8.mainloop()
  def sda(level=0):
     txtd7.delete(1.0, END)
     def sda2(br,sd,level):
       br = br.replace("|",',')
       sd1=sd
       level=level+1

       if "," in br:
         br=br.split(",")
       #jnxbcnbnm имена
         for br in br:
           br = br.replace(" ",'')
           br = br.replace("(",' ')
           br = br.replace("=",'')
           br = br.replace(")",'')
           if  " " in br:
             if  "<" in br or  ">" in br:
                br = br.replace("<",'')
                br = br.replace(">",'')
             # txtd7.insert(INSERT,"отчиска завершина")
                sd=sd1
                a,b=br.split()
                if a in sd :
                  continue
                else: 
                    number1 = collection.count_documents({'Package': a})
                    if number1==0:
                        if level==1:
                          txtd7.insert(INSERT,"|"+'___' * level + 'Package:'+' ')
                          txtd7.insert(INSERT,a,"likes") 
                          txtd7.insert(INSERT,'\n')
                        else:
                          txtd7.insert(INSERT,"|"+'       ' * level +"|"+ '_' * 3 + 'Package:'+' ')
                          txtd7.insert(INSERT,a,"likes") 
                          txtd7.insert(INSERT,'\n')
                   #    txtd7.insert(INSERT,'Даного пакета нет в базе данных')
                    else:
                       for channel in collection.find({'Package': a}):# поиск покета
                        bq=channel['Package']
                        Bw=channel['Version']
                        be=channel['Architecture']
                        if 'Depends' in channel: # проверка содержит ли  данный пакет зависимости 
                          br=channel['Depends']
                          if level==1:
                           txtd7.insert(INSERT,"|"+'___' * level + 'Package:'+' ')
                           txtd7.insert(INSERT,bq,"likes") 
                           txtd7.insert(INSERT,'\n')
                          else:
                           txtd7.insert(INSERT,"|"+'       ' * level +"|"+ '_' * 3 + 'Package:'+' ')
                           txtd7.insert(INSERT,bq,"likes") 
                           txtd7.insert(INSERT,'\n')
                          sd1.append(bq)
                          sd=sd1 
                          if 'PreDepends' in channel: # проверка содержит ли  данный пакет непосредственой зависимости 
                            ba=channel['PreDepends']
                            br=br+","+ba
                            sda2(br,sd,level)
                          else:
                            sda2(br,sd,level)  
                        else: # если нет зависимости
                           if 'PreDepends' in channel:# проверка содержит ли  данный пакет непосредственой зависимости 
                              ba=channel['PreDepends']
                              if level==1:
                               txtd7.insert(INSERT,"|"+'___' * level + 'Package:'+' ')
                               txtd7.insert(INSERT,bq,"likes") 
                               txtd7.insert(INSERT,'\n')
                              else:
                               txtd7.insert(INSERT,"|"+'       ' * level +"|"+ '_' * 3 + 'Package:'+' ')
                               txtd7.insert(INSERT,bq,"likes") 
                               txtd7.insert(INSERT,'\n')
                              sd1.append(bq)
                              sd=sd1
                              br=ba
                          
                              sda2(br,sd,level)
                           else:  # если нет непосредствеой зависимости
                             if level==1:
                               txtd7.insert(INSERT,"|"+'___' * level + 'Package:'+' ')
                               txtd7.insert(INSERT,bq,"likes") 
                               txtd7.insert(INSERT,'\n')
                             else:
                                txtd7.insert(INSERT,"|"+'       ' * level +"|"+ '_' * 3 + 'Package:'+' ')
                                txtd7.insert(INSERT,bq,"likes") 
                                txtd7.insert(INSERT,'\n')  
                             sd1.append(bq)  
                           #      
                      
             else:
            #  txtd7.insert(INSERT,"отчиска завершина")
                sd=sd1
                a,b=br.split()
                if a in sd :
                  continue
                else: 
                  number1 = collection.count_documents({'$and': [{'Package': a},{'Version': b}]})
                  if number1==0:
                    if level==1:
                      txtd7.insert(INSERT,"|"+'___' * level + 'Package:'+' ')
                      txtd7.insert(INSERT,a,"likes") 
                      txtd7.insert(INSERT,'\n')
                    else:
                      txtd7.insert(INSERT,"|"+'       ' * level +"|"+ '_' * 3 + 'Package:'+' ')
                      txtd7.insert(INSERT,a,"likes") 
                      txtd7.insert(INSERT,'\n') 
                 # txtd7.insert(INSERT,'Даного пакета нет в базе данных')
                  else:
                   for channel in collection.find({'$and': [{'Package': a},{'Version': b}]}):# поиск покета
                    bq=channel['Package']
                    Bw=channel['Version']
                    be=channel['Architecture']
                    if 'Depends' in channel: # проверка содержит ли  данный пакет зависимости 
                      br=channel['Depends']
                      if level==1:
                        txtd7.insert(INSERT,"|"+'___' * level + 'Package:'+' ')
                        txtd7.insert(INSERT,bq,"likes") 
                        txtd7.insert(INSERT,'\n')
                      else:
                        txtd7.insert(INSERT,"|"+'       ' * level +"|"+ '_' * 3 + 'Package:'+' ')
                        txtd7.insert(INSERT,bq,"likes") 
                        txtd7.insert(INSERT,'\n') 
                      sd1.append(bq)
                      sd=sd1
                    
                      if 'PreDepends' in channel: # проверка содержит ли  данный пакет непосредственой зависимости 
                        ba=channel['PreDepends']
                        br=br+","+ba
                        sda2(br,sd,level)
                      else:
                        sda2(br,sd,level)  
                    else: # если нет зависимости
                      if 'PreDepends' in channel:# проверка содержит ли  данный пакет непосредственой зависимости 
                        ba=channel['PreDepends']
                        if level==1:
                          txtd7.insert(INSERT,"|"+'___' * level + 'Package:'+' ')
                          txtd7.insert(INSERT,bq,"likes") 
                          txtd7.insert(INSERT,'\n')
                        else:
                          txtd7.insert(INSERT,"|"+'       ' * level +"|"+ '_' * 3 + 'Package:'+' ')
                          txtd7.insert(INSERT,bq,"likes") 
                          txtd7.insert(INSERT,'\n') 
                      
                        sd1.append(bq,level)
                        sd=sd1
                        br=ba
                        sda2(br,sd,level) 
                      else:  # если нет непосредствеой зависимости  
                        if level==1:
                          txtd7.insert(INSERT,"|"+'___' * level + 'Package:'+' ')
                          txtd7.insert(INSERT,bq,"likes") 
                          txtd7.insert(INSERT,'\n')
                        else:
                          txtd7.insert(INSERT,"|"+'       ' * level +"|"+ '_' * 3 + 'Package:'+' ')
                          txtd7.insert(INSERT,bq,"likes") 
                          txtd7.insert(INSERT,'\n') 
                        sd1.append(bq)    
                      
           else:    
              br = br.replace(" ",'')
              br = br.replace("(",' ')
              br = br.replace("=",'')
              br = br.replace(")",'')
              br = br.replace("<",'')
              br = br.replace(">",'')
              if br in sd :
                continue
              else: 
                br=br
                number1 = collection.count_documents({'Package': br})
                if number1==0:
                    if level==1:
                      txtd7.insert(INSERT,"|"+'___' * level + 'Package:'+' ')
                      txtd7.insert(INSERT,br,"likes") 
                      txtd7.insert(INSERT,'\n')
                    else:
                      txtd7.insert(INSERT,"|"+'       ' * level +"|"+ '_' * 3 + 'Package:'+' ')
                      txtd7.insert(INSERT,br,"likes") 
                      txtd7.insert(INSERT,'\n') 
                 #   txtd7.insert(INSERT,'Даного пакета нет в базе данных')
                else:
                 for channel in collection.find({'Package': br}):# поиск покета
                  bq=channel['Package']
                  Bw=channel['Version']
                  be=channel['Architecture']
                  if 'Depends' in channel: # проверка содержит ли  данный пакет зависимости 
                    br=channel['Depends']
                    if level==1:
                      txtd7.insert(INSERT,"|"+'___' * level + 'Package:'+' ')
                      txtd7.insert(INSERT,bq,"likes") 
                      txtd7.insert(INSERT,'\n')
                    else:
                      txtd7.insert(INSERT,"|"+'       ' * level +"|"+ '_' * 3 + 'Package:'+' ')
                      txtd7.insert(INSERT,bq,"likes") 
                      txtd7.insert(INSERT,'\n') 
                    sd1.append(bq)
                    sd=sd1
                  
                    if 'PreDepends' in channel: # проверка содержит ли  данный пакет непосредственой зависимости 
                     ba=channel['PreDepends']
                     br=br+","+ba
                     sda2(br,sd,level)
                    else:
                      sda2(br,sd,level) 
                  else: # если нет зависимости
                    if 'PreDepends' in channel:# проверка содержит ли  данный пакет непосредственой зависимости 
                     ba=channel['PreDepends']
                     if level==1:
                        txtd7.insert(INSERT,"|"+'___' * level + 'Package:'+' ')
                        txtd7.insert(INSERT,bq,"likes") 
                        txtd7.insert(INSERT,'\n')
                     else:
                        txtd7.insert(INSERT,"|"+'       ' * level +"|"+ '_' * 3 + 'Package:'+' ')
                        txtd7.insert(INSERT,bq,"likes") 
                        txtd7.insert(INSERT,'\n') 
                     br=ba
                     sd1.append(bq)
                     sd=sd1
                   
                     sda2(br,sd,level)
                   
                    else:  # если нет непосредствеой зависимости  
                      if level==1:
                        txtd7.insert(INSERT,"|"+'___' * level + 'Package:'+' ')
                        txtd7.insert(INSERT,bq,"likes") 
                        txtd7.insert(INSERT,'\n')
                      else:
                        txtd7.insert(INSERT,"|"+'       ' * level +"|"+ '_' * 3 + 'Package:'+' ')
                        txtd7.insert(INSERT,bq,"likes") 
                        txtd7.insert(INSERT,'\n') 
                      sd1.append(bq)
                      sd=sd1          
       else:
           br = br.replace(" ",'')
           br = br.replace("(",' ')
           br = br.replace("=",'')
           br = br.replace(")",'')
           if  " " in br:
             if  "<" in br or  ">" in br:
                br = br.replace("<",'')
                br = br.replace(">",'')
               # txtd7.insert(INSERT,"отчиска завершина")
                sd=sd1
                z,b=br.split()
                if z in sd :
                  return
                else: 
                    number1 = collection.count_documents({'Package': z})
                    if number1==0:
                        if level==1:
                          txtd7.insert(INSERT,"|"+'___' * level + 'Package:'+' ')
                          txtd7.insert(INSERT,z,"likes") 
                          txtd7.insert(INSERT,'\n')
                        else:
                          txtd7.insert(INSERT,"|"+'       ' * level +"|"+ '_' * 3 + 'Package:'+' ')
                          txtd7.insert(INSERT,z,"likes") 
                          txtd7.insert(INSERT,'\n') 
                   #     txtd7.insert(INSERT,'Даного пакета нет в базе данных')
                    else:
                     for channel in collection.find({'Package': z}):# поиск покета
                       bq=channel['Package']
                       Bw=channel['Version']
                       be=channel['Architecture']
                       if 'Depends' in channel: # проверка содержит ли  данный пакет зависимости 
                         br=channel['Depends']
                         if level==1:
                            txtd7.insert(INSERT,"|"+'___' * level + 'Package:'+' ')
                            txtd7.insert(INSERT,bq,"likes") 
                            txtd7.insert(INSERT,'\n')
                         else:
                            txtd7.insert(INSERT,"|"+'       ' * level +"|"+ '_' * 3 + 'Package:'+' ')
                            txtd7.insert(INSERT,bq,"likes") 
                            txtd7.insert(INSERT,'\n') 
                         sd1.append(bq)
                         sd=sd1
                       
                         if 'PreDepends' in channel: # проверка содержит ли  данный пакет непосредственой зависимости 
                           ba=channel['PreDepends']
                           br=br+","+ba
                           sda2(br,sd,level)
                         else:
                           sda2(br,sd,level)  
                       else: # если нет зависимости
                         if 'PreDepends' in channel:# проверка содержит ли  данный пакет непосредственой зависимости 
                            ba=channel['PreDepends']
                            if level==1:
                              txtd7.insert(INSERT,"|"+'___' * level + 'Package:'+' ')
                              txtd7.insert(INSERT,bq,"likes") 
                              txtd7.insert(INSERT,'\n')
                            else:
                              txtd7.insert(INSERT,"|"+'       ' * level +"|"+ '_' * 3 + 'Package:'+' ')
                              txtd7.insert(INSERT,bq,"likes") 
                              txtd7.insert(INSERT,'\n') 
                            sd1.append(bq)
                            sd=sd1
                            br=ba
                          
                            sda2(br,sd,level)
                         else:  # если нет непосредствеой зависимости  
                            if level==1:
                              txtd7.insert(INSERT,"|"+'___' * level + 'Package:'+' ')
                              txtd7.insert(INSERT,bq,"likes") 
                              txtd7.insert(INSERT,'\n')
                            else:
                              txtd7.insert(INSERT,"|"+'       ' * level +"|"+ '_' * 3 + 'Package:'+' ')
                              txtd7.insert(INSERT,bq,"likes") 
                              txtd7.insert(INSERT,'\n') 
                            sd1.append(bq)       
                      
             else:
              #  txtd7.insert(INSERT,"отчиска завершина")
                sd=sd1
                a,b=br.split()
                if a in sd :
                  return
                else: 
                  number1 = collection.count_documents({'$and': [{'Package': a},{'Version': b}]})
                  if number1==0:
                    if level==1:
                      txtd7.insert(INSERT,"|"+'___' * level + 'Package:'+' ')
                      txtd7.insert(INSERT,a,"likes") 
                      txtd7.insert(INSERT,'\n')
                    else:
                      txtd7.insert(INSERT,"|"+'       ' * level +"|"+ '_' * 3 + 'Package:'+' ')
                      txtd7.insert(INSERT,a,"likes") 
                      txtd7.insert(INSERT,'\n') 
                 #   txtd7.insert(INSERT,'Даного пакета нет в базе данных')
                  else:
                   for channel in collection.find({'$and': [{'Package': a},{'Version': b}]}):# поиск покета
                    bq=channel['Package']
                    Bw=channel['Version']
                    be=channel['Architecture']
                    if 'Depends' in channel: # проверка содержит ли  данный пакет зависимости 
                      br=channel['Depends']
                      if level==1:
                          txtd7.insert(INSERT,"|"+'___' * level + 'Package:'+' ')
                          txtd7.insert(INSERT,bq,"likes") 
                          txtd7.insert(INSERT,'\n')
                      else:
                        txtd7.insert(INSERT,"|"+'       ' * level +"|"+ '_' * 3 + 'Package:'+' ')
                        txtd7.insert(INSERT,bq,"likes") 
                        txtd7.insert(INSERT,'\n') 
                      sd1.append(bq,level)
                      sd=sd1
                     
                      if 'PreDepends' in channel: # проверка содержит ли  данный пакет непосредственой зависимости 
                        ba=channel['PreDepends']
                        br=br+","+ba
                        sda2(br,sd,level)
                      else:
                        sda2(br,sd,level)  
                    else: # если нет зависимости
                      if 'PreDepends' in channel:# проверка содержит ли  данный пакет непосредственой зависимости 
                        ba=channel['PreDepends']
                        if level==1:
                          txtd7.insert(INSERT,"|"+'___' * level + 'Package:'+' ')
                          txtd7.insert(INSERT,bq,"likes") 
                          txtd7.insert(INSERT,'\n')
                        else:
                          txtd7.insert(INSERT,"|"+'       ' * level +"|"+ '_' * 3 + 'Package:'+' ')
                          txtd7.insert(INSERT,bq,"likes") 
                          txtd7.insert(INSERT,'\n') 
                        sd1.append(bq)
                        sd=sd1
                        br=ba
                      
                        sda2(br,sd,level) 
                      else:  # если нет непосредствеой зависимости 
                        if level==1:
                          txtd7.insert(INSERT,"|"+'___' * level + 'Package:'+' ')
                          txtd7.insert(INSERT,bq,"likes") 
                          txtd7.insert(INSERT,'\n')
                        else:
                          txtd7.insert(INSERT,"|"+'       ' * level +"|"+ '_' * 3 + 'Package:'+' ')
                          txtd7.insert(INSERT,bq,"likes") 
                          txtd7.insert(INSERT,'\n') 
                        sd1.append(bq)            
                      
           else:    
              br = br.replace(" ",'')
              br = br.replace("(",' ')
              br = br.replace("=",'')
              br = br.replace(")",'')
              br = br.replace("<",'')
              br = br.replace(">",'')
              if br in sd :
                return
              else: 
                br=br
                number1 = collection.count_documents({'Package': br})
                if number1==0:
                    if level==1:
                      txtd7.insert(INSERT,"|"+'___' * level + 'Package:'+' ')
                      txtd7.insert(INSERT,br,"likes") 
                      txtd7.insert(INSERT,'\n')
                    else:
                      txtd7.insert(INSERT,"|"+'       ' * level +"|"+ '_' * 3 + 'Package:'+' ')
                      txtd7.insert(INSERT,br,"likes") 
                      txtd7.insert(INSERT,'\n') 
              #    txtd7.insert(INSERT,'Даного пакета нет в базе данных')
                else:
                 for channel in collection.find({'Package': br}):# поиск покета
                  bq=channel['Package']
                  Bw=channel['Version']
                  be=channel['Architecture']
                  if 'Depends' in channel: # проверка содержит ли  данный пакет зависимости 
                    br=channel['Depends']
                    if level==1:
                      txtd7.insert(INSERT,"|"+'___' * level + 'Package:'+' ')
                      txtd7.insert(INSERT,bq,"likes") 
                      txtd7.insert(INSERT,'\n')
                    else:
                        txtd7.insert(INSERT,"|"+'       ' * level +"|"+ '_' * 3 + 'Package:'+' ')
                        txtd7.insert(INSERT,bq,"likes") 
                        txtd7.insert(INSERT,'\n') 
                    sd1.append(bq)
                    sd=sd1
                  
                    if 'PreDepends' in channel: # проверка содержит ли  данный пакет непосредственой зависимости 
                     ba=channel['PreDepends']
                     br=br+","+ba
                     sda2(br,sd,level)
                    else:
                      sda2(br,sd,level) 
                  else: # если нет зависимости
                        if 'PreDepends' in channel:# проверка содержит ли  данный пакет непосредственой зависимости 
                            ba=channel['PreDepends']
                            if level==1:
                               txtd7.insert(INSERT,"|"+'___' * level + 'Package:'+' ')
                               txtd7.insert(INSERT,bq,"likes") 
                               txtd7.insert(INSERT,'\n')
                            else:
                              txtd7.insert(INSERT,"|"+'       ' * level +"|"+ '_' * 3 + 'Package:'+' ')
                              txtd7.insert(INSERT,bq,"likes") 
                              txtd7.insert(INSERT,'\n') 
                            br=ba
                            sd1.append(bq)
                            sd=sd1
                            
                            sda2(br,sd,level)
                        else:  # если нет непосредствеой зависимости  
                             if level==1:
                               txtd7.insert(INSERT,"|"+'___' * level + 'Package:'+' ')
                               txtd7.insert(INSERT,bq,"likes") 
                               txtd7.insert(INSERT,'\n')
                             else:
                                txtd7.insert(INSERT,"|"+'       ' * level +"|"+ '_' * 3 + 'Package:'+' ')
                                txtd7.insert(INSERT,bq,"likes") 
                                txtd7.insert(INSERT,'\n') 
                             sd1.append(bq)
                             sd=sd1
       txtd7.tag_config("likes", foreground='#d2d2d2', underline=1) 
       txtd7.tag_bind("likes", "<1>",namepac7)                              
     PackageName = PackageName_entry1.get()
     versionName = versionName_entry1.get()
     number1 = collection.count_documents({'$and': [{'Package': PackageName},{'Version': versionName}]})
     if number1==0:
         txtd7.insert(INSERT,'Даного пакета нет в базе данных')
     else:
        channel = collection.find_one({'$and': [{'Package': PackageName},{'Version': versionName}]})# поиск покета с именем которы ведёт пользователь
        bq=channel['Package']
        Bw=channel['Version']
        be=channel['Architecture']
        if 'Depends' in channel: # проверка содержит ли  данный пакет зависимости 
         br=channel['Depends'] 
         txtd7.insert(INSERT,'      |' * level   + 'Package:'+' ')
         txtd7.insert(INSERT,bq,"likes")
         txtd7.insert(INSERT,'\n')
         sd=bq
         sd=sd.split(",")
         if 'PreDepends' in channel:# проверка содержит ли  данный пакет непосредственой зависимости 
           ba=channel['PreDepends']
           br=br+","+ba
         
           sda2(br,sd,level)
         else:
          
           sda2(br,sd,level)
        else: # если нет зависимости
          if 'PreDepends' in channel:# проверка содержит ли  данный пакет непосредственой зависимости 
            ba=channel['PreDepends']
            txtd7.insert(INSERT,'      |' * level+ 'Package:'+' ')# вывод имени пакета
            txtd7.insert(INSERT,bq,"likes")
            txtd7.insert(INSERT,'\n')
            sd=bq
            sd=sd.split(",")
            br=ba
          
            sda2(br,sd,level)
          else:  # если нет непосредствеой зависимости    
           txtd7.insert(INSERT,'      |' * level  + 'Package:'+' ') # вывод имени пакета
           txtd7.insert(INSERT,bq,"likes")
           txtd7.insert(INSERT,'\n')
          #txtd7.insert(INSERT,"у даного пакета нет зависимости")
  root7=Tk()
  def btnReturn7(e):
   sda()
 
  def limitSizeDay2(event):
    value = PackageName_entry1.get()
    if len(value)>1:
      send7_btn.config(state='normal')
      root7.bind('<Return>', btnReturn7)
    else:
      send7_btn.config(state='disabled')
  root7.title(' Поиск дерева зависимости пакета')
  root7['bg'] ='#2c2c2c'
  root7.geometry('640x730')
  root7.resizable(width=False,height=False)
  Package_label=Label(root7,text='имя пакета',font=("Arial Bold", 10), bg='#2c2c2c',fg='#d2d2d2',padx=10,pady=8)
  Package_label.pack()
  PackageName_entry1 = Entry(root7,bg='white',fg='#2c2c2c', font=("Arial Bold", 10))
  PackageName_entry1.pack()
  Package_label=Label(root7,text='Версия пакета',font=("Arial Bold", 10), bg='#2c2c2c',fg='#d2d2d2',padx=10,pady=8)
  Package_label.pack()
  versionName_entry1 = Entry(root7,bg='white',fg='#2c2c2c', font=("Arial Bold", 10))
  versionName_entry1.pack()
  send7_btn= Button(root7,text="Найти",bg='#2c2c2c',fg='#d2d2d2',command = sda)
  send7_btn.pack(padx=15,pady=10)
  txtd7 = scrolledtext.ScrolledText(root7,width=60,height=30,font=("Arial Bold", 10), bg='#2c2c2c',fg='#d2d2d2',padx=10,pady=8, cursor="hand2")
  txtd7.pack()
  root7.bind("<Enter>",  limitSizeDay2)
  root7.mainloop()
    
  
  
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


def btn_2clicked():  # открытие файла
  # создание глобальной переменой
  global name 
  name = tk.filedialog.askopenfilename() # открытие окна выбора файла 
  txtd5.insert(INSERT,name) # Отправка сообщения об открытии файла в главное окно

# авторизация...
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
    cluster = MongoClient(text)
    try:
     print("MongoDB version is %s" %
             cluster.server_info()['version'])
     messagebox.showinfo('подключение успешно пройдено',f'{username},{Password},{Address}')
    except pymongo.errors.OperationFailure as error:
      messagebox.showinfo("\nНет подключения к серверу","\nПроверьте введённые данные")
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
 
 
 #Отправка в бд
def homea():
  global name  
  name=name.split("/")
  name= name.pop()
  name="/home/user/"+name 
def btn_clicked():
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
      txtd5.insert(INSERT,"Файл не найден. Зайдите в настройки и выберите файл"+"\n")
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
      txtd5.insert(INSERT,"Файл не найден. Зайдите в настройки и выберите файл"+"\n")
 except UnboundLocalError: 
    txtd5.insert(INSERT,"\n"+"Выберите другой файл,данный неправильного формата"+"\n")         
    os.remove(name + 's.json')
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