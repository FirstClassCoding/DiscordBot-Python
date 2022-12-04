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
        current_time['text'] = getTime('time')
        current_date['text'] = getTime('date')
        time.sleep(0.1)

def runBot(menu = '' , item = '' , value = '' , datenow = '' , timenow = ''):
    #Bot Ready
    @bot.event
    async def on_ready():
        print(bot.user.name , "Started!\nDay : %s"%getTime('date'))

    @bot.event
    async def on_message(message):
        if message.content == ('item!Check'):
            read_Data = pd.read_excel('Data.xlsx')
            embed = discord.Embed(title = 'รายการไอเท็ม' , description = read_Data , color = 0x000000)
            #embed.set_thumbnail(url = '')
            await message.channel.send(embed=embed)
            print('*-*-*-*-*-*-*-*-*-*-*-*-*-*\nDay : %s'%getTime('date'))
            print('Time : %s'%getTime('time'))
            print('Command :',message.content)

    #ได้รับไอเท็ม
    def receivedPost():
        bot.loop.create_task(sendReceivedPost())

    async def sendReceivedPost():
        await bot.wait_until_ready()
        roomID = 985092458683707432
        text = 'ได้รับ ' + str(item) + ' จำนวน ' + str(value) + ' ชิ้น'
        date = 'วันที่ ' + str(datenow) + ' เวลา ' + str(timenow)
        embed = discord.Embed(title = date , description = text , color = 0x000000)
        channel = bot.get_channel(roomID)
        await channel.send(embed=embed)

    #สูญเสียไอเท็ม
    def lostPost():
        bot.loop.create_task(sendLostPost())

    async def sendLostPost():
        await bot.wait_until_ready()
        roomID = 985092458683707432
        text = 'สูญเสีย ' + str(item) + ' จำนวน ' + str(value) + ' ชิ้น'
        date = 'วันที่ ' + str(datenow) + ' เวลา ' + str(timenow)
        embed = discord.Embed(title = date , description = text , color = 0x000000)
        channel = bot.get_channel(roomID)
        await channel.send(embed=embed)

    if menu == 'add':
        return receivedPost()
    elif menu == 'remove':
        return lostPost()

    bot.run('') # Enter token here

class history:
    def add(item , value):
        readHistory = pd.read_excel('History.xlsx')
        newHistory = pd.DataFrame({'Date' : [getTime('date')] , 'Time' : [getTime('time')] , 'Item List' : [item] , 'Value' : [value]})
        updateHistory = [readHistory , newHistory]
        resultHistory = pd.concat(updateHistory)
        writeHistory = pd.ExcelWriter('History.xlsx',engine='xlsxwriter')
        resultHistory.to_excel(writeHistory,index = False)
        writeHistory.save()

class data:
    def add(item , value):
        readData = pd.read_excel('Data.xlsx')
        getData = readData.loc[item,['Value']]
        datatoNum = int(getData)
        newData = datatoNum + value
        readData.loc[item,['Value']] = [newData]
        editData = readData
        writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
        editData.to_excel(writeData,index = False)
        writeData.save()
        return newData

    def remove(item , value):
        readData = pd.read_excel('Data.xlsx')
        getData = readData.loc[item,['Value']]
        datatoNum = int(getData)
        newData = datatoNum - value
        readData.loc[item,['Value']] = [newData]
        editData = readData
        writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
        editData.to_excel(writeData,index = False)
        writeData.save()
        return newData

#เมนูอัพเดทข้อมูล
def updateData():
    readData = pd.read_excel('Data.xlsx')
    getGaosData = readData.iloc[0,1]
    getMuradData = readData.iloc[1,1]
    getRainbowCrystalData = readData.iloc[2,1]
    getBlackArmorData = readData.iloc[3,1]

    lb_GaosValue['text'] = getGaosData
    lb_MuradValue['text'] = getMuradData
    lb_RainbowCrystalValue['text'] = getRainbowCrystalData
    lb_BlackArmorValue['text'] = getBlackArmorData

#เพิ่มจำนวนหัวใจกาออส
def addGaos():
    line = 0
    name = 'หัวใจกาออส'
    Value = int(get_Value.get())

    history.add(name , Value)
    lb_GaosValue['text'] = data.add(line , Value)
    runBot('add' , name , Value , getTime('date') , getTime('time'))

#ลดจำนวนหัวใจกาออส
def removeGaos():
    line = 0
    name = 'หัวใจกาออส'
    Value = int(get_Value.get())
    NValue = '-' + str(Value)

    history.add(name , NValue)
    lb_GaosValue['text'] = data.remove(line , Value)
    runBot('remove' , name , Value , getTime('date') , getTime('time'))

#เพิ่มจำนวนแร่ไฟ
def addMurad():
    line = 1
    name = 'แร่ไฟ'
    Value = int(get_Value.get())

    history.add(name , Value)
    lb_MuradValue['text'] = data.add(line , Value)
    runBot('add' , name , Value , getTime('date') , getTime('time'))

#ลดจำนวนแร่ไฟ
def removeMurad():
    line = 1
    name = 'แร่ไฟ'
    Value = int(get_Value.get())
    NValue = '-' + str(Value)

    history.add(name , NValue)
    lb_MuradValue['text'] = data.remove(line , Value)
    runBot('remove' , name , Value , getTime('date') , getTime('time'))

#เพิ่มจำนวนคริสตัลรุ้ง
def addRainbowCrystal():
    line = 2
    name = 'คริสตัลรุ้ง'
    Value = int(get_Value.get())
    
    history.add(name , Value)
    lb_RainbowCrystalValue['text'] = data.add(line , Value)
    runBot('add' , name , Value , getTime('date') , getTime('time'))

#ลดจำนวนคริสตัลรุ้ง
def removeRainbowCrystal():
    line = 2
    name = 'คริสตัลรุ้ง'
    Value = int(get_Value.get())
    NValue = '-' + str(Value)

    history.add(name , NValue)
    lb_RainbowCrystalValue['text'] = data.remove(line , Value)
    runBot('remove' , name , Value , getTime('date') , getTime('time'))

#เพิ่มจำนวนเกราะดำ
def addBlackArmor():
    line = 3
    name = 'เกราะดำ'
    Value = int(get_Value.get())
    
    history.add(name , Value)
    lb_BlackArmorValue['text'] = data.add(line , Value)
    runBot('add' , name , Value , getTime('date') , getTime('time'))

#ลดจำนวนเกราะดำ
def removeBlackArmor():
    line = 3
    name = 'เกราะดำ'
    Value = int(get_Value.get())
    NValue = '-' + str(Value)

    history.add(name , NValue)
    lb_BlackArmorValue['text'] = data.remove(line , Value)
    runBot('remove' , name , Value , getTime('date') , getTime('time'))

#กำหนด Prefix
bot = commands.Bot(command_prefix = 'item!')

#ปรับการตั้งค่าโปรแกรม
app = tk.Tk()
app.title('Item for Sell and Pricelist')
app.resizable(0,0)
app.geometry('250x250')
icon = tk.PhotoImage(file = 'diamond_carrot.png')
app.iconphoto(False,icon)

menuBar = tk.Menu(master = app)

#File Menu
menu_File = tk.Menu(master = menuBar , tearoff = 0)
menu_File.add_command(label = 'Load File' , command = updateData)
#menu_File.add_command(label = 'Open')
#menu_File.add_command(label = 'Save')
#menu_File.add_command(label = 'Save as')
#menu_File.add_separator()
#menu_File.add_command(label = 'Exit' , command = app.quit)
menuBar.add_cascade(label = 'File' , menu = menu_File)

#Edit Menu
menu_Edit = tk.Menu(master = menuBar , tearoff = 0)
#menu_Edit.add_command(label = 'Undo' , command = test)
#menu_Edit.add_command(label = 'Redo')
#menuBar.add_cascade(label = 'Edit' , menu = menu_Edit)

#date
lb_date = tk.Label(master = app  , text = 'Current Date :')
lb_date.grid(row = 0 , column = 0 , padx = (5,0) , pady = (5,0))
lb_date.config(font = ('Tahoma' , 10))

current_date = tk.Label(master = app , text = 'Waiting...')
current_date.grid(row = 0 , column = 1 , padx = (0,5) , pady = (5,0))
current_date.config(font = ('Tahoma' , 10))

#time
lb_time = tk.Label(master = app , text = 'Current Time :')
lb_time.grid(row = 1 , column = 0 , padx = (5,0) , pady = (0,0))
lb_time.config(font = ('Tahoma' , 10))

current_time = tk.Label(master = app , text = 'Waiting...')
current_time.grid(row = 1 , column = 1 , padx = (0,5) , pady = (0,0))
current_time.config(font = ('Tahoma' , 10))

#รายการไอเท็ม
lb_Itemlist = tk.Label(master = app , text = 'รายการไอเท็ม')
lb_Itemlist.grid(row = 2 , column = 0 , padx = (5,5) , pady = (10,0))
lb_Itemlist.config(font = ('Tahoma' , 10))

lb_Gaos = tk.Label(master = app , text = 'หัวใจกาออส')
lb_Gaos.grid(row = 3 , column = 0 , padx = (5,5) , pady = (5,0))
lb_Gaos.config(font = ('Tahoma' , 10))

lb_Murad = tk.Label(master = app , text = 'แร่ไฟ')
lb_Murad.grid(row = 4 , column = 0 , padx = (5,5) , pady = (0,0))
lb_Murad.config(font = ('Tahoma' , 10))

lb_RainbowCrystal = tk.Label(master = app , text = 'คริสตัลรุ้ง')
lb_RainbowCrystal.grid(row = 5 , column = 0 , padx = (5,5) , pady = (0,0))
lb_RainbowCrystal.config(font = ('Tahoma' , 10))

lb_BlackArmor = tk.Label(master = app , text = 'เกราะดำ')
lb_BlackArmor.grid(row = 6 , column = 0 , padx = (5,5) , pady = (0,0))
lb_BlackArmor.config(font = ('Tahoma' , 10))

#จำนวนที่มี
lb_Value = tk.Label(master = app , text = 'จำนวน')
lb_Value.grid(row = 2 , column = 1 , padx = (5,5) , pady = (10,0))
lb_Value.config(font = ('Tahoma' , 10))

lb_GaosValue = tk.Label(master = app , text = '-')
lb_GaosValue.grid(row = 3 , column = 1 , padx = (5,5) , pady = (5,0))
lb_GaosValue.config(font = ('Tahoma' , 10))

lb_MuradValue = tk.Label(master = app , text = '-')
lb_MuradValue.grid(row = 4 , column = 1 , padx = (5,5) , pady = (0,0))
lb_MuradValue.config(font = ('Tahoma' , 10))

lb_RainbowCrystalValue = tk.Label(master = app , text = '-')
lb_RainbowCrystalValue.grid(row = 5 , column = 1 , padx = (5,5) , pady = (0,0))
lb_RainbowCrystalValue.config(font = ('Tahoma' , 10))

lb_BlackArmorValue = tk.Label(master = app , text = '-')
lb_BlackArmorValue.grid(row = 6 , column = 1 , padx = (5,5) , pady = (0,0))
lb_BlackArmorValue.config(font = ('Tahoma' , 10))

#ปุ่มเพิ่มไอเท็ม
bt_addGaos = tk.Button(master = app , text = 'เพิ่ม' , command = addGaos)
bt_addGaos.grid(row = 3 , column = 2 , padx = (0,0) , pady = (5,0))
bt_addGaos.config(font = ('Tahoma' , 8))

bt_addMurad = tk.Button(master = app , text = 'เพิ่ม' , command = addMurad)
bt_addMurad.grid(row = 4 , column = 2 , padx = (0,0) , pady = (0,0))
bt_addMurad.config(font = ('Tahoma' , 8))

bt_addRainbowCrystal = tk.Button(master = app , text = 'เพิ่ม' , command = addRainbowCrystal)
bt_addRainbowCrystal.grid(row = 5 , column = 2 , padx = (0,0) , pady = (0,0))
bt_addRainbowCrystal.config(font = ('Tahoma' , 8))

bt_addBlackArmor = tk.Button(master = app , text = 'เพิ่ม' , command = addBlackArmor)
bt_addBlackArmor.grid(row = 6 , column = 2 , padx = (0,0) , pady = (0,0))
bt_addBlackArmor.config(font = ('Tahoma' , 8))

#ปุ่มลดไอเท็ม
bt_removeGaos = tk.Button(master = app , text = 'ลด' , command = removeGaos)
bt_removeGaos.grid(row = 3 , column = 3 , padx = (15,0) , pady = (5,0))
bt_removeGaos.config(font = ('Tahoma' , 8))

bt_removeMurad = tk.Button(master = app , text = 'ลด' , command = removeMurad)
bt_removeMurad.grid(row = 4 , column = 3 , padx = (15,0) , pady = (0,0))
bt_removeMurad.config(font = ('Tahoma' , 8))

bt_removeRainbowCrystal = tk.Button(master = app , text = 'ลด' , command = removeRainbowCrystal)
bt_removeRainbowCrystal.grid(row = 5 , column = 3 , padx = (15,0) , pady = (0,0))
bt_removeRainbowCrystal.config(font = ('Tahoma' , 8))

bt_removeBlackArmor = tk.Button(master = app , text = 'ลด' , command = removeBlackArmor)
bt_removeBlackArmor.grid(row = 6 , column = 3 , padx = (15,0) , pady = (0,0))
bt_removeBlackArmor.config(font = ('Tahoma' , 8))

#ช่องใส่จำนวน
lb_getValue = tk.Label(master = app , text = 'จำนวนที่ต้องการ')
lb_getValue.grid(row = 7 , column = 0 , padx = (5,0) , pady = (20,0))
lb_getValue.config(font = ('Tahoma' , 10))

get_Value = tk.Entry(master = app , width = 5)
get_Value.grid(row = 7 , column = 1 , padx = (5,5) , pady = (20,0))

threading.Thread(target = runTime).start()
threading.Thread(target = runBot).start()

app.config(menu = menuBar)
app.mainloop()

