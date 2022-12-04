import discord
from discord.ext import commands
from datetime import datetime
from getTime import getTime
import tkinter as tk
import pandas as pd
import asyncio
import time
import threading
import os

def runTime():
    while True:
        run_time['text'] = getTime('time')
        run_date['text'] = getTime('date')
        time.sleep(0.1)

def runBot():
    async def post():
        await bot.wait_until_ready()
        roomID = int(entry1_1.get())
        text = str(entry2_1.get())
        channel = bot.get_channel(roomID)
        while not bot.is_closed():
            await channel.send(text)
            await asyncio.sleep(0.1)
            break

    @bot.event
    async def on_ready() : #เมื่อระบบพร้อมใช้งาน
        print(bot.user.name , "Started!\nDay : %s"%getTime('date')) #แสดงผลใน CMD

    def textPost():
        bot.loop.create_task(post())

    #Post
    bt3_1 = tk.Button(master = app , text = 'Post' , command = textPost)
    bt3_1.grid(row = 4 , column = 0 , columnspan = 2 , padx = (0,0) , pady = (0,0))
    bt3_1.config(font = ('Tahoma' , 10))

    #bot.loop.create_task(post())
    bot.run('')

#กำหนด Prefix
bot = commands.Bot(command_prefix='!')

#ปรับการตั้งค่าโปรแกรม
app = tk.Tk()
app.title('Bot Controller')
app.resizable(0,0)
app.geometry('300x300')

#date
lb_date = tk.Label(master = app  , text = 'Run Date :')
lb_date.grid(row = 0 , column = 0 , padx = (5,0) , pady = (5,0))
lb_date.config(font = ('Tahoma' , 10))

run_date = tk.Label(master = app , text = 'Waiting...')
run_date.grid(row = 0 , column = 1 , padx = (0,5) , pady = (5,0))
run_date.config(font = ('Tahoma' , 10))

#time
lb_time = tk.Label(master = app , text = 'Run Time :')
lb_time.grid(row = 1 , column = 0 , padx = (5,0) , pady = (0,0))
lb_time.config(font = ('Tahoma' , 10))

run_time = tk.Label(master = app , text = 'Waiting...')
run_time.grid(row = 1 , column = 1 , padx = (0,5) , pady = (0,0))
run_time.config(font = ('Tahoma' , 10))

#Enter RoomID
lb1_1 = tk.Label(master = app , text = 'Enter Text Room ID')
lb1_1.grid(row = 2 , column = 0 , columnspan = 2 , padx = (0,0) , pady = (0,0))
lb1_1.config(font = ('Tahoma' , 10))

entry1_1 = tk.Entry(master = app , width = 20)
entry1_1.grid(row = 2 , column = 3 , padx = (0,0) ,pady = (0,0))

#Enter Text
lb2_1 = tk.Label(master = app , text = 'Enter Text')
lb2_1.grid(row = 3 , column = 0 , columnspan = 2 , padx = (0,0) , pady = (0,0))
lb2_1.config(font = ('Tahoma' , 10))

entry2_1 = tk.Entry(master = app , width = 20)
entry2_1.grid(row = 3 , column = 3 , padx = (0,0) , pady = (0,0))

'''#Post
bt3_1 = tk.Button(master = app , text = 'Post' , command = '')
bt3_1.grid(row = 4 , column = 0 , columnspan = 2 , padx = (0,0) , pady = (0,0))
bt3_1.config(font = ('Tahoma' , 10))'''

'''@bot.event
async def on_message(message) :
    if message.content.startswith('!announce') :
        data = str(message.content)
        tags = str(data[10:])
        
        if (tags.startswith('here')) :

            here_text = len('here')+3
            lenroomid = 18
            find_roomid = tags[here_text:]
            room = find_roomid[:lenroomid]
            roomID = int(room)
            
            channel = bot.get_channel(roomID)

            lentext = len('!announce') + here_text + lenroomid + 2
            text = str(data[lentext:])
            
            embed = discord.Embed(title = '' , description = (text) , color = 0xFF7F50)
            await channel.send('@here' , embed=embed)

            print('*-*-*-*-*-*-*-*-*\nRoomID :',roomID,'\nOriginal Message :',data,'\nText :',text,'\nDay :',day)
        
        elif (tags.startswith('everyone')) :
            
            here_text = len('everyone')+3
            lenroomid = 18
            find_roomid = tags[here_text:]
            room = find_roomid[:lenroomid]
            roomID = int(room)
            
            channel = bot.get_channel(roomID)

            lentext = len('!announce') + here_text + lenroomid + 2
            text = str(data[lentext:])
            
            embed = discord.Embed(title = '' , description = (text) , color = 0xFF7F50)
            await channel.send('@everyone' , embed=embed)

            print('*-*-*-*-*-*-*-*-*\nRoomID :',roomID,'\nOriginal Message :',data,'\nText :',text,'\nDay :',day)

    elif message.content.startswith('!pic') :
        data = str(message.content)
        tags = str(data[5:])

        if (tags.startswith('here')) :

            here_text = len('here')+3
            lenroomid = 18
            find_roomid = tags[here_text:]
            room = find_roomid[:lenroomid]
            roomID = int(room)
            
            channel = bot.get_channel(roomID)

            lentext = len('!pic') + here_text + lenroomid + 2
            text = str(data[lentext:])
            
            embed = discord.Embed(title = '' , description = '' , color = 0xFF7F50)
            embed.set_image(url = text)
            
            await channel.send('@here' , embed=embed)

            print('*-*-*-*-*-*-*-*-*\nRoomID :',roomID,'\nOriginal Message :',data,'\nText :',text,'\nDay :',day)
        
        elif (tags.startswith('everyone')) :
            
            here_text = len('everyone')+3
            lenroomid = 18
            find_roomid = tags[here_text:]
            room = find_roomid[:lenroomid]
            roomID = int(room)
            
            channel = bot.get_channel(roomID)

            lentext = len('!pic') + here_text + lenroomid + 2
            text = str(data[lentext:])
            
            embed = discord.Embed(title = '' , description = '' , color = 0xFF7F50)
            embed.set_image(url = text)
            
            await channel.send('@everyone' , embed=embed)

            print('*-*-*-*-*-*-*-*-*\nRoomID :',roomID,'\nOriginal Message :',data,'\nText :',text,'\nDay :',day)
'''

'''
@bot.event
async def on_message(message) :
    if message.content == ('!announce') :
        channel = bot.get_channel()
        embed = discord.Embed(title = "" , description = "" , color=0x00FF00)
        embed.set_image(url = "")
        embed.set_thumbnail(url = "https://media.discordapp.net/attachments/934475055063261194/973168740873142322/M_Icon-01.png?width=472&height=472")
        await channel.send('@here' , embed=embed)
'''
'''
@bot.command(pass_context=True)
async def Text(ctx):
    channel = bot.get_channel(966592243953725480)
    await channel.send('Test')
'''

threading.Thread(target = runTime).start()
threading.Thread(target = runBot).start()

#app.config(menu = menuBar)
app.mainloop()

#bot.loop.create_task(post())
