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
   #messagebox.showinfo("Ошибка","\nНет подключения к серверу. Проверьте введённые данные\n")
  else:
     messagebox.showerror("Ошибка","\nНет подключения к серверу. Откройте меню настройки и выберите пункт сервер и введите данные о сервере\n")
 except FileNotFoundError:
    messagebox.showerror("Ошибка","\nНет подключения к серверу. Откройте меню настройки и выберите пункт сервер и введите данные о сервере\n") 
def btn_bd7():
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
     BDconect()                                
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