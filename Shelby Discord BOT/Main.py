import discord
from discord.ext import commands
from datetime import datetime
from getTime import getTime
import time
import pandas as pd

day = str(getTime('date'))

#1
def tori():
    readData = pd.read_excel('Data.xlsx')
    newData = pd.DataFrame({'Name' : ['Tori'] , 'Date' : [day]})
    updateData = [readData , newData]
    result = pd.concat(updateData)
    writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
    result.to_excel(writeData,index = False)
    writeData.save()
    print('Tori Has been update!')

#2
def bella():
    readData = pd.read_excel('Data.xlsx')
    newData = pd.DataFrame({'Name' : ['Bella'] , 'Date' : [day]})
    updateData = [readData , newData]
    result = pd.concat(updateData)
    writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
    result.to_excel(writeData,index = False)
    writeData.save()
    print('Bella Has been update!')

#3
def white():
    readData = pd.read_excel('Data.xlsx')
    newData = pd.DataFrame({'Name' : ['White'] , 'Date' : [day]})
    updateData = [readData , newData]
    result = pd.concat(updateData)
    writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
    result.to_excel(writeData,index = False)
    writeData.save()
    print('White Has been update!')

#4
def ozone():
    readData = pd.read_excel('Data.xlsx')
    newData = pd.DataFrame({'Name' : ['Ozone'] , 'Date' : [day]})
    updateData = [readData , newData]
    result = pd.concat(updateData)
    writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
    result.to_excel(writeData,index = False)
    writeData.save()
    print('Ozone Has been update!')

#5
def run():
    readData = pd.read_excel('Data.xlsx')
    newData = pd.DataFrame({'Name' : ['Run'] , 'Date' : [day]})
    updateData = [readData , newData]
    result = pd.concat(updateData)
    writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
    result.to_excel(writeData,index = False)
    writeData.save()
    print('Run Has been update!')

#6
def somchai():
    readData = pd.read_excel('Data.xlsx')
    newData = pd.DataFrame({'Name' : ['Somchai'] , 'Date' : [day]})
    updateData = [readData , newData]
    result = pd.concat(updateData)
    writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
    result.to_excel(writeData,index = False)
    writeData.save()
    print('Somchai Has been update!')

#7
def lucino():
    readData = pd.read_excel('Data.xlsx')
    newData = pd.DataFrame({'Name' : ['Lucino'] , 'Date' : [day]})
    updateData = [readData , newData]
    result = pd.concat(updateData)
    writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
    result.to_excel(writeData,index = False)
    writeData.save()
    print('Lucino Has been update!')

#8
def boy():
    readData = pd.read_excel('Data.xlsx')
    newData = pd.DataFrame({'Name' : ['Boy'] , 'Date' : [day]})
    updateData = [readData , newData]
    result = pd.concat(updateData)
    writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
    result.to_excel(writeData,index = False)
    writeData.save()
    print('Boy Has been update!')

#9
def olym():
    readData = pd.read_excel('Data.xlsx')
    newData = pd.DataFrame({'Name' : ['Olym'] , 'Date' : [day]})
    updateData = [readData , newData]
    result = pd.concat(updateData)
    writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
    result.to_excel(writeData,index = False)
    writeData.save()
    print('Olym Has been update!')

#10
def somtuy():
    readData = pd.read_excel('Data.xlsx')
    newData = pd.DataFrame({'Name' : ['Somtuy'] , 'Date' : [day]})
    updateData = [readData , newData]
    result = pd.concat(updateData)
    writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
    result.to_excel(writeData,index = False)
    writeData.save()
    print('Somtuy Has been update!')

#11
def tang():
    readData = pd.read_excel('Data.xlsx')
    newData = pd.DataFrame({'Name' : ['Tang'] , 'Date' : [day]})
    updateData = [readData , newData]
    result = pd.concat(updateData)
    writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
    result.to_excel(writeData,index = False)
    writeData.save()
    print('Tang Has been update!')

#12
def kern():
    readData = pd.read_excel('Data.xlsx')
    newData = pd.DataFrame({'Name' : ['Kern'] , 'Date' : [day]})
    updateData = [readData , newData]
    result = pd.concat(updateData)
    writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
    result.to_excel(writeData,index = False)
    writeData.save()
    print('Kern Has been update!')

#13
def somii():
    readData = pd.read_excel('Data.xlsx')
    newData = pd.DataFrame({'Name' : ['Somii'] , 'Date' : [day]})
    updateData = [readData , newData]
    result = pd.concat(updateData)
    writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
    result.to_excel(writeData,index = False)
    writeData.save()
    print('Somii Has been update!')

#14
def somtui():
    readData = pd.read_excel('Data.xlsx')
    newData = pd.DataFrame({'Name' : ['Somtui'] , 'Date' : [day]})
    updateData = [readData , newData]
    result = pd.concat(updateData)
    writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
    result.to_excel(writeData,index = False)
    writeData.save()
    print('Somtui Has been update!')

#15
def greentea():
    readData = pd.read_excel('Data.xlsx')
    newData = pd.DataFrame({'Name' : ['GreenTea'] , 'Date' : [day]})
    updateData = [readData , newData]
    result = pd.concat(updateData)
    writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
    result.to_excel(writeData,index = False)
    writeData.save()
    print('GreenTea Has been update!')

#16
def artee():
    readData = pd.read_excel('Data.xlsx')
    newData = pd.DataFrame({'Name' : ['Artee'] , 'Date' : [day]})
    updateData = [readData , newData]
    result = pd.concat(updateData)
    writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
    result.to_excel(writeData,index = False)
    writeData.save()
    print('Artee Has been update!')

#17
def es():
    readData = pd.read_excel('Data.xlsx')
    newData = pd.DataFrame({'Name' : ['Es'] , 'Date' : [day]})
    updateData = [readData , newData]
    result = pd.concat(updateData)
    writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
    result.to_excel(writeData,index = False)
    writeData.save()
    print('Es Has been update!')

#18
def bob():
    readData = pd.read_excel('Data.xlsx')
    newData = pd.DataFrame({'Name' : ['Bob'] , 'Date' : [day]})
    updateData = [readData , newData]
    result = pd.concat(updateData)
    writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
    result.to_excel(writeData,index = False)
    writeData.save()
    print('Bob Has been update!')

#19
def boi():
    readData = pd.read_excel('Data.xlsx')
    newData = pd.DataFrame({'Name' : ['Boi'] , 'Date' : [day]})
    updateData = [readData , newData]
    result = pd.concat(updateData)
    writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
    result.to_excel(writeData,index = False)
    writeData.save()
    print('Boi Has been update!')

#20
def chaom():
    readData = pd.read_excel('Data.xlsx')
    newData = pd.DataFrame({'Name' : ['Chaom'] , 'Date' : [day]})
    updateData = [readData , newData]
    result = pd.concat(updateData)
    writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
    result.to_excel(writeData,index = False)
    writeData.save()
    print('Chaom Has been update!')

#21
def mhok():
    readData = pd.read_excel('Data.xlsx')
    newData = pd.DataFrame({'Name' : ['Mhok'] , 'Date' : [day]})
    updateData = [readData , newData]
    result = pd.concat(updateData)
    writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
    result.to_excel(writeData,index = False)
    writeData.save()
    print('Mhok Has been update!')

#22
def david():
    readData = pd.read_excel('Data.xlsx')
    newData = pd.DataFrame({'Name' : ['David'] , 'Date' : [day]})
    updateData = [readData , newData]
    result = pd.concat(updateData)
    writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
    result.to_excel(writeData,index = False)
    writeData.save()
    print('David Has been update!')

#23
def logan():
    readData = pd.read_excel('Data.xlsx')
    newData = pd.DataFrame({'Name' : ['Logan'] , 'Date' : [day]})
    updateData = [readData , newData]
    result = pd.concat(updateData)
    writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
    result.to_excel(writeData,index = False)
    writeData.save()
    print('Logan Has been update!')

#24
def bubee():
    readData = pd.read_excel('Data.xlsx')
    newData = pd.DataFrame({'Name' : ['Bubee'] , 'Date' : [day]})
    updateData = [readData , newData]
    result = pd.concat(updateData)
    writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
    result.to_excel(writeData,index = False)
    writeData.save()
    print('Bubee Has been update!')

#25
def rojin():
    readData = pd.read_excel('Data.xlsx')
    newData = pd.DataFrame({'Name' : ['Rojin'] , 'Date' : [day]})
    updateData = [readData , newData]
    result = pd.concat(updateData)
    writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
    result.to_excel(writeData,index = False)
    writeData.save()
    print('Rojin Has been update!')

#26
def haji():
    readData = pd.read_excel('Data.xlsx')
    newData = pd.DataFrame({'Name' : ['Haji'] , 'Date' : [day]})
    updateData = [readData , newData]
    result = pd.concat(updateData)
    writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
    result.to_excel(writeData,index = False)
    writeData.save()
    print('Haji Has been update!')

#27
def ford():
    readData = pd.read_excel('Data.xlsx')
    newData = pd.DataFrame({'Name' : ['Ford'] , 'Date' : [day]})
    updateData = [readData , newData]
    result = pd.concat(updateData)
    writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
    result.to_excel(writeData,index = False)
    writeData.save()
    print('Ford Has been update!')

#28
def shouta():
    readData = pd.read_excel('Data.xlsx')
    newData = pd.DataFrame({'Name' : ['Shouta'] , 'Date' : [day]})
    updateData = [readData , newData]
    result = pd.concat(updateData)
    writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
    result.to_excel(writeData,index = False)
    writeData.save()
    print('Shouta Has been update!')

#29
def mica():
    readData = pd.read_excel('Data.xlsx')
    newData = pd.DataFrame({'Name' : ['Mica'] , 'Date' : [day]})
    updateData = [readData , newData]
    result = pd.concat(updateData)
    writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
    result.to_excel(writeData,index = False)
    writeData.save()
    print('Mica Has been update!')

#30
def mikey():
    readData = pd.read_excel('Data.xlsx')
    newData = pd.DataFrame({'Name' : ['Mikey'] , 'Date' : [day]})
    updateData = [readData , newData]
    result = pd.concat(updateData)
    writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
    result.to_excel(writeData,index = False)
    writeData.save()
    print('Mikey Has been update!')

#31
def mari():
    readData = pd.read_excel('Data.xlsx')
    newData = pd.DataFrame({'Name' : ['Mari'] , 'Date' : [day]})
    updateData = [readData , newData]
    result = pd.concat(updateData)
    writeData = pd.ExcelWriter('Data.xlsx',engine='xlsxwriter')
    result.to_excel(writeData,index = False)
    writeData.save()
    print('Mari Has been update!')
    
'''
def test():
    readData = pd.read_excel('Locker.xlsx')
    Test = str(readData.iloc[18,0])
    TesttoNum = int(Test[5:])
    editTest = int(getData[11:])
    editData = str('Test_%d' %editTest)
    fixData = readData.replace([Test],[editData])
    writeData = pd.ExcelWriter('Locker.xlsx',engine='xlsxwriter')
    fixData.to_excel(writeData,index = False)
    writeData.save()'''

'''
def test():
    readData = pd.read_excel('ResultData.xlsx')
    newData = pd.DataFrame({'ชื่อ' : ['Test'] , 'ยอดส่ง' : ['Test']})
    updateData = [readData , newData]
    result = pd.concat(updateData)
    writeData = pd.ExcelWriter('ResultData.xlsx',engine='xlsxwriter')
    result.to_excel(writeData,index = False)
    writeData.save()
    print('Test Has been update!')'''

'''
client = discord.Client()
guild = discord.Guild

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith('_'):
        cmd = message.content.split()[0].replace("_","")
        if len(message.content.split()) > 1:
            parameters = message.content.split()[1:]

if cmd == 'scan':
    data = pd.DataFrame(columns = ['content' , 'time' , 'author'])

    def is_command(msg):
        if len(msg.content) == 0:
            return False
        elif msg.content.split()[0] == '_scan':
            return True
        else:
            return False
    @client.command()
    async for msg in message.channel.history(limit=10000):
        if msg.author != client.user:
            if not is_command(msg):
                data = data.append({'content' : msg.content,
                                    'time' : msg.created_at,
                                    'author' : msg.author.name} , ignore_index = True)
            if len(data) == limit:
                break
            writeData = pd.ExcelWriter('Chatlog.xlsx',engine='xlsxwriter')
            data.to_excel(writeData,index = False)
            writeData.save()
'''   
    
bot = commands.Bot(command_prefix='sb!')
#กำหนด Prefix

@bot.event
async def on_ready() : #เมื่อระบบพร้อมใช้งาน
    print(bot.user.name , "Started!\nDay : %s"%day) #แสดงผลใน CMD

@bot.event
async def on_message(message) :
    if message.content == ('sb!Text') :
        test = str(message.channel)
        sms = str(message.content)
        sms2 = str(sms[7:])
        print(test)
        #await message.channel.send('Hello')

    elif message.content == ('sb!Test') :
        embed = discord.Embed(title = "SHELBY" , description = "Inprogress!\nComing Soon!!" , color=0x000000)
        embed.set_thumbnail(url = "https://media.discordapp.net/attachments/936369950686314579/952557305302511736/Logo_SB_SS4.png?width=472&height=472")
        await message.channel.send(embed=embed)

    elif message.content == ('sb!Help') :
        #await ctx.send('***การใช้งานบอท***\n\n- ใช้คำสั่งนำหน้า sb! ทุกครั้งเพื่อใช้งานบอทแล้วตัวแรกหลังเครื่องหมาย ! ต้องเป็นตัวพิมพ์ใหญ่เท่านั้น\n\nชุดคำสั่ง\n- การเช็คชื่อส่งของให้พิมพ์ sb! แล้วตามด้วยชื่อนำหน้าหรือเช็คได้ที่ sb!Slot\n- sb!Slot แสดงรายชื่อสล็อตแก๊ง\n- sb!Help เมนูช่วยเหลือ/แนะนำการใช้งาน\n- sb!Checklist เช็คข้อมูลในระบบ \n- sb!Checkdate เช็ควันที่ในระบบ')
        embed = discord.Embed(title = "SHELBY HELP / การใช้งานบอท" , description = "ชุดคำสั่ง\n- sb!Help เมนูช่วยเหลือ\n- sb!Slot แสดงรายชื่อสล็อตแก๊ง\n- sb!Checklist เรียกดูข้อมูลการส่งของ (ปิดปรับปรุง)\n- sb!Checkdate เช็ควันที่ในระบบ\n- sb!Checklocker เรียกดูของแก๊ง\n- sb!HelpLocker เมนูช่วยเหลือในการบันทึกข้อมูลของในตู้แก๊ง" , color=0x000000)
        embed.set_thumbnail(url = "https://media.discordapp.net/attachments/936369950686314579/952557305302511736/Logo_SB_SS4.png?width=472&height=472")
        await message.channel.send(embed=embed)

    elif message.content == ('sb!HelpLocker') :    
        embed = discord.Embed(title = "SHELBY LOCKER HELP / การใช้งานบอทตู้แก๊ง" , description = "- คำสั่งทุกคำสั่งขึ้นต้นด้วย Locker! โดยไม่เว้นวรรคแล้วตามด้วยชื่อของในตู้โดยดูได้ที่ sb!Checklocker\n\n- หลังจากพิมพ์คำสั่งเสร็จสิ้นให้พิมพ์จำนวนตัวเลขต่อจากคำสั่งเพื่อทำการเพิ่ม/ลดยอดของในตู้โดย\n\n- หากต้องการเพิ่มให้มีเครื่องหมาย + นำหน้าหรือไม่มีก็ได้ เช่น Locker!KFC+10 หรือ Locker!KFC10\n\n- หากต้องการลดต้องมีเครื่องหมาย - เสมอ เช่น Locker!KFC-10" , color=0x000000)
        embed.set_thumbnail(url = "https://media.discordapp.net/attachments/936369950686314579/952557305302511736/Logo_SB_SS4.png?width=472&height=472")
        await message.channel.send(embed=embed)

    elif message.content == ('sb!Slot') :
        embed = discord.Embed(title = "SHELBY SLOT" , description = "1. Tori Charlotte\n2. Bella Rose\n3. White SB\n4. Ozone Binladen\n5. Run MorningStar\n6. Somchai Parangbai\n7. Lucino Espresso\n8. Boy Butler\n9. Olym Binlahden\n10. Somtuy Serpent\n11. Tang Zii\n12. Bang Kern\n13. Somii Rose\n14. Somtui Louisan\n15. GreenTea Xakos\n16. Artee\n17. Es Presso\n18. Bob Phranakhon\n19. Boi Phrankhon\n20. Chaom Kan\n21. Mhok Robinson\n22. David Namoys\n23. Logan Cullen\n24. Bubee Inboso\n25. Rojin Black\n26. Haji City\n27. Ford Blacklist\n28. Shouta Biggory\n29. Mica Black\n30. Mikey Kung\n31. Mari Mala\n\nUpdate : 21/04/2565" , color=0x000000)
        embed.set_thumbnail(url = "https://media.discordapp.net/attachments/936369950686314579/952557305302511736/Logo_SB_SS4.png?width=472&height=472")
        await message.channel.send(embed=embed)

    elif message.content == ('sb!Checklist') :
        dataBase = pd.read_excel('Data.xlsx')
        embed = discord.Embed(title = "Checklist" , description = dataBase , color=0x000000)
        #embed.set_thumbnail(url = "https://media.discordapp.net/attachments/936369950686314579/952557305302511736/Logo_SB_SS4.png?width=472&height=472")
        await message.channel.send(embed=embed)

    elif message.content == ('sb!Checkdate') :
        await message.channel.send(day)

    elif message.content == ('sb!Callhistory10day') :
        History = pd.read_excel('ResultData.xlsx')
        embed = discord.Embed(title = "ยอดการส่งของ 10 ครั้งของวันที่ 12/04/65 - 21/04/65" , description = History , color=0x000000)
        #embed.set_thumbnail(url = "https://media.discordapp.net/attachments/936369950686314579/952557305302511736/Logo_SB_SS4.png?width=472&height=472")
        await message.channel.send(embed=embed)
        
    elif message.content == ('sb!Checklocker') :
        Locker = pd.read_excel('Locker.xlsx')
        embed = discord.Embed(title = "ตู้แก๊ง" , description = Locker , color=0x000000)
        #embed.set_thumbnail(url = "https://media.discordapp.net/attachments/936369950686314579/952557305302511736/Logo_SB_SS4.png?width=472&height=472")
        await message.channel.send(embed=embed)

    #เงินเขียว
    elif message.content.startswith('Locker!เงินเขียว') :
        getData = str(message.content)
        getDatatoNum = int(getData[16:])
        print('Locker Getting Data เงินเขียว from User is :',getDatatoNum,'Date :',day)
        readData = pd.read_excel('Locker.xlsx')
        print('กำลังอ่านข้อมูล...')
        callData = str(readData.iloc[0,0])
        print('ข้อมูลปัจจุบันที่อ่านได้คือ',callData)
        callDatatoNum = int(callData[10:])
        editTest = callDatatoNum + getDatatoNum
        editData = str('เงินเขียว_%d' %editTest)
        print('ข้อมูลหลังการคำนวณ',editTest)
        fixData = readData.replace([callData],[editData])
        writeData = pd.ExcelWriter('Locker.xlsx',engine='xlsxwriter')
        fixData.to_excel(writeData,index = False)
        writeData.save()
        
        readData = pd.read_excel('Locker.xlsx')
        callData = str(readData.iloc[0,0])
        print('ข้อมูลหลังการอัพเดท',callData)
        await message.channel.send('อัพเดทข้อมูลเสร็จสิ้น ตรวจสอบข้อมูลได้ที่ sb!Checklocker')
        print('การอัพเดทข้อมูล เงินเขียว เสร็จสิ้น!')

    #เงินแดง
    elif message.content.startswith('Locker!เงินแดง') :
        getData = str(message.content)
        getDatatoNum = int(getData[14:])
        print('Locker Getting Data เงินแดง from User is :',getDatatoNum,'Date :',day)
        readData = pd.read_excel('Locker.xlsx')
        print('กำลังอ่านข้อมูล...')
        callData = str(readData.iloc[1,0])
        print('ข้อมูลปัจจุบันที่อ่านได้คือ',callData)
        callDatatoNum = int(callData[8:])
        editTest = callDatatoNum + getDatatoNum
        editData = str('เงินแดง_%d' %editTest)
        print('ข้อมูลหลังการคำนวณ',editTest)
        fixData = readData.replace([callData],[editData])
        writeData = pd.ExcelWriter('Locker.xlsx',engine='xlsxwriter')
        fixData.to_excel(writeData,index = False)
        writeData.save()
        
        readData = pd.read_excel('Locker.xlsx')
        callData = str(readData.iloc[1,0])
        print('ข้อมูลหลังการอัพเดท',callData)
        await message.channel.send('อัพเดทข้อมูลเสร็จสิ้น ตรวจสอบข้อมูลได้ที่ sb!Checklocker')
        print('การอัพเดทข้อมูล เงินแดง เสร็จสิ้น!')

    #Pain25
    elif message.content.startswith('Locker!Pain25') :
        getData = str(message.content)
        getDatatoNum = int(getData[13:])
        print('Locker Getting Data Pain25 from User is :',getDatatoNum,'Date :',day)
        readData = pd.read_excel('Locker.xlsx')
        print('กำลังอ่านข้อมูล...')
        callData = str(readData.iloc[2,0])
        print('ข้อมูลปัจจุบันที่อ่านได้คือ',callData)
        callDatatoNum = int(callData[7:])
        editTest = callDatatoNum + getDatatoNum
        editData = str('Pain25_%d' %editTest)
        print('ข้อมูลหลังการคำนวณ',editTest)
        fixData = readData.replace([callData],[editData])
        writeData = pd.ExcelWriter('Locker.xlsx',engine='xlsxwriter')
        fixData.to_excel(writeData,index = False)
        writeData.save()
        
        readData = pd.read_excel('Locker.xlsx')
        callData = str(readData.iloc[2,0])
        print('ข้อมูลหลังการอัพเดท',callData)
        await message.channel.send('อัพเดทข้อมูลเสร็จสิ้น ตรวจสอบข้อมูลได้ที่ sb!Checklocker')
        print('การอัพเดทข้อมูล Pain25 เสร็จสิ้น!')

    #Pain40
    elif message.content.startswith('Locker!Pain40') :
        getData = str(message.content)
        getDatatoNum = int(getData[13:])
        print('Locker Getting Data Pain40 from User is :',getDatatoNum,'Date :',day)
        readData = pd.read_excel('Locker.xlsx')
        print('กำลังอ่านข้อมูล...')
        callData = str(readData.iloc[3,0])
        print('ข้อมูลปัจจุบันที่อ่านได้คือ',callData)
        callDatatoNum = int(callData[7:])
        editTest = callDatatoNum + getDatatoNum
        editData = str('Pain40_%d' %editTest)
        print('ข้อมูลหลังการคำนวณ',editTest)
        fixData = readData.replace([callData],[editData])
        writeData = pd.ExcelWriter('Locker.xlsx',engine='xlsxwriter')
        fixData.to_excel(writeData,index = False)
        writeData.save()
        
        readData = pd.read_excel('Locker.xlsx')
        callData = str(readData.iloc[3,0])
        print('ข้อมูลหลังการอัพเดท',callData)
        await message.channel.send('อัพเดทข้อมูลเสร็จสิ้น ตรวจสอบข้อมูลได้ที่ sb!Checklocker')
        print('การอัพเดทข้อมูล Pain40 เสร็จสิ้น!')

    #AED
    elif message.content.startswith('Locker!AED') :
        getData = str(message.content)
        getDatatoNum = int(getData[10:])
        print('Locker Getting Data AED from User is :',getDatatoNum,'Date :',day)
        readData = pd.read_excel('Locker.xlsx')
        print('กำลังอ่านข้อมูล...')
        callData = str(readData.iloc[4,0])
        print('ข้อมูลปัจจุบันที่อ่านได้คือ',callData)
        callDatatoNum = int(callData[4:])
        editTest = callDatatoNum + getDatatoNum
        editData = str('AED_%d' %editTest)
        print('ข้อมูลหลังการคำนวณ',editTest)
        fixData = readData.replace([callData],[editData])
        writeData = pd.ExcelWriter('Locker.xlsx',engine='xlsxwriter')
        fixData.to_excel(writeData,index = False)
        writeData.save()
        
        readData = pd.read_excel('Locker.xlsx')
        callData = str(readData.iloc[4,0])
        print('ข้อมูลหลังการอัพเดท',callData)
        await message.channel.send('อัพเดทข้อมูลเสร็จสิ้น ตรวจสอบข้อมูลได้ที่ sb!Checklocker')
        print('การอัพเดทข้อมูล AED เสร็จสิ้น!')

    #เกราะ
    elif message.content.startswith('Locker!เกราะ') :
        getData = str(message.content)
        getDatatoNum = int(getData[12:])
        print('Locker Getting Data เกราะ from User is :',getDatatoNum,'Date :',day)
        readData = pd.read_excel('Locker.xlsx')
        print('กำลังอ่านข้อมูล...')
        callData = str(readData.iloc[5,0])
        print('ข้อมูลปัจจุบันที่อ่านได้คือ',callData)
        callDatatoNum = int(callData[6:])
        editTest = callDatatoNum + getDatatoNum
        editData = str('เกราะ_%d' %editTest)
        print('ข้อมูลหลังการคำนวณ',editTest)
        fixData = readData.replace([callData],[editData])
        writeData = pd.ExcelWriter('Locker.xlsx',engine='xlsxwriter')
        fixData.to_excel(writeData,index = False)
        writeData.save()
        
        readData = pd.read_excel('Locker.xlsx')
        callData = str(readData.iloc[5,0])
        print('ข้อมูลหลังการอัพเดท',callData)
        await message.channel.send('อัพเดทข้อมูลเสร็จสิ้น ตรวจสอบข้อมูลได้ที่ sb!Checklocker')
        print('การอัพเดทข้อมูล เกราะ เสร็จสิ้น!')

    #แร่โพแทสเซียม
    elif message.content.startswith('Locker!แร่โพแทสเซียม') :
        getData = str(message.content)
        getDatatoNum = int(getData[20:])
        print('Locker Getting Data แร่โพแทสเซียม from User is :',getDatatoNum,'Date :',day)
        readData = pd.read_excel('Locker.xlsx')
        print('กำลังอ่านข้อมูล...')
        callData = str(readData.iloc[6,0])
        print('ข้อมูลปัจจุบันที่อ่านได้คือ',callData)
        callDatatoNum = int(callData[14:])
        editTest = callDatatoNum + getDatatoNum
        editData = str('แร่โพแทสเซียม_%d' %editTest)
        print('ข้อมูลหลังการคำนวณ',editTest)
        fixData = readData.replace([callData],[editData])
        writeData = pd.ExcelWriter('Locker.xlsx',engine='xlsxwriter')
        fixData.to_excel(writeData,index = False)
        writeData.save()
        
        readData = pd.read_excel('Locker.xlsx')
        callData = str(readData.iloc[6,0])
        print('ข้อมูลหลังการอัพเดท',callData)
        await message.channel.send('อัพเดทข้อมูลเสร็จสิ้น ตรวจสอบข้อมูลได้ที่ sb!Checklocker')
        print('การอัพเดทข้อมูล แร่โพแทสเซียม เสร็จสิ้น!')

    #ปูน
    elif message.content.startswith('Locker!ปูน') :
        getData = str(message.content)
        getDatatoNum = int(getData[10:])
        print('Locker Getting Data ปูน from User is :',getDatatoNum,'Date :',day)
        readData = pd.read_excel('Locker.xlsx')
        print('กำลังอ่านข้อมูล...')
        callData = str(readData.iloc[7,0])
        print('ข้อมูลปัจจุบันที่อ่านได้คือ',callData)
        callDatatoNum = int(callData[4:])
        editTest = callDatatoNum + getDatatoNum
        editData = str('ปูน_%d' %editTest)
        print('ข้อมูลหลังการคำนวณ',editTest)
        fixData = readData.replace([callData],[editData])
        writeData = pd.ExcelWriter('Locker.xlsx',engine='xlsxwriter')
        fixData.to_excel(writeData,index = False)
        writeData.save()
        
        readData = pd.read_excel('Locker.xlsx')
        callData = str(readData.iloc[7,0])
        print('ข้อมูลหลังการอัพเดท',callData)
        await message.channel.send('อัพเดทข้อมูลเสร็จสิ้น ตรวจสอบข้อมูลได้ที่ sb!Checklocker')
        print('การอัพเดทข้อมูล ปูน เสร็จสิ้น!')

    #สายไฟ
    elif message.content.startswith('Locker!สายไฟ') :
        getData = str(message.content)
        getDatatoNum = int(getData[12:])
        print('Locker Getting Data สายไฟ from User is :',getDatatoNum,'Date :',day)
        readData = pd.read_excel('Locker.xlsx')
        print('กำลังอ่านข้อมูล...')
        callData = str(readData.iloc[8,0])
        print('ข้อมูลปัจจุบันที่อ่านได้คือ',callData)
        callDatatoNum = int(callData[6:])
        editTest = callDatatoNum + getDatatoNum
        editData = str('สายไฟ_%d' %editTest)
        print('ข้อมูลหลังการคำนวณ',editTest)
        fixData = readData.replace([callData],[editData])
        writeData = pd.ExcelWriter('Locker.xlsx',engine='xlsxwriter')
        fixData.to_excel(writeData,index = False)
        writeData.save()
        
        readData = pd.read_excel('Locker.xlsx')
        callData = str(readData.iloc[8,0])
        print('ข้อมูลหลังการอัพเดท',callData)
        await message.channel.send('อัพเดทข้อมูลเสร็จสิ้น ตรวจสอบข้อมูลได้ที่ sb!Checklocker')
        print('การอัพเดทข้อมูล สายไฟ เสร็จสิ้น!')

    #เมล็ดกัญชา
    elif message.content.startswith('Locker!เมล็ดกัญชา') :
        getData = str(message.content)
        getDatatoNum = int(getData[17:])
        print('Locker Getting Data เมล็ดกัญชา from User is :',getDatatoNum,'Date :',day)
        readData = pd.read_excel('Locker.xlsx')
        print('กำลังอ่านข้อมูล...')
        callData = str(readData.iloc[9,0])
        print('ข้อมูลปัจจุบันที่อ่านได้คือ',callData)
        callDatatoNum = int(callData[11:])
        editTest = callDatatoNum + getDatatoNum
        editData = str('เมล็ดกัญชา_%d' %editTest)
        print('ข้อมูลหลังการคำนวณ',editTest)
        fixData = readData.replace([callData],[editData])
        writeData = pd.ExcelWriter('Locker.xlsx',engine='xlsxwriter')
        fixData.to_excel(writeData,index = False)
        writeData.save()
        
        readData = pd.read_excel('Locker.xlsx')
        callData = str(readData.iloc[9,0])
        print('ข้อมูลหลังการอัพเดท',callData)
        await message.channel.send('อัพเดทข้อมูลเสร็จสิ้น ตรวจสอบข้อมูลได้ที่ sb!Checklocker')
        print('การอัพเดทข้อมูล เมล็ดกัญชา เสร็จสิ้น!')

    #ใบกัญชา
    elif message.content.startswith('Locker!ใบกัญชา') :
        getData = str(message.content)
        getDatatoNum = int(getData[14:])
        print('Locker Getting Data ใบกัญชา from User is :',getDatatoNum,'Date :',day)
        readData = pd.read_excel('Locker.xlsx')
        print('กำลังอ่านข้อมูล...')
        callData = str(readData.iloc[10,0])
        print('ข้อมูลปัจจุบันที่อ่านได้คือ',callData)
        callDatatoNum = int(callData[8:])
        editTest = callDatatoNum + getDatatoNum
        editData = str('ใบกัญชา_%d' %editTest)
        print('ข้อมูลหลังการคำนวณ',editTest)
        fixData = readData.replace([callData],[editData])
        writeData = pd.ExcelWriter('Locker.xlsx',engine='xlsxwriter')
        fixData.to_excel(writeData,index = False)
        writeData.save()
        
        readData = pd.read_excel('Locker.xlsx')
        callData = str(readData.iloc[10,0])
        print('ข้อมูลหลังการอัพเดท',callData)
        await message.channel.send('อัพเดทข้อมูลเสร็จสิ้น ตรวจสอบข้อมูลได้ที่ sb!Checklocker')
        print('การอัพเดทข้อมูล ใบกัญชา เสร็จสิ้น!')

    #แพ็คกัญชา
    elif message.content.startswith('Locker!แพ็คกัญชา') :
        getData = str(message.content)
        getDatatoNum = int(getData[16:])
        print('Locker Getting Data แพ็คกัญชา from User is :',getDatatoNum,'Date :',day)
        readData = pd.read_excel('Locker.xlsx')
        print('กำลังอ่านข้อมูล...')
        callData = str(readData.iloc[11,0])
        print('ข้อมูลปัจจุบันที่อ่านได้คือ',callData)
        callDatatoNum = int(callData[10:])
        editTest = callDatatoNum + getDatatoNum
        editData = str('แพ็คกัญชา_%d' %editTest)
        print('ข้อมูลหลังการคำนวณ',editTest)
        fixData = readData.replace([callData],[editData])
        writeData = pd.ExcelWriter('Locker.xlsx',engine='xlsxwriter')
        fixData.to_excel(writeData,index = False)
        writeData.save()
        
        readData = pd.read_excel('Locker.xlsx')
        callData = str(readData.iloc[11,0])
        print('ข้อมูลหลังการอัพเดท',callData)
        await message.channel.send('อัพเดทข้อมูลเสร็จสิ้น ตรวจสอบข้อมูลได้ที่ sb!Checklocker')
        print('การอัพเดทข้อมูล แพ็คกัญชา เสร็จสิ้น!')

    #คริสตัลแดง
    elif message.content.startswith('Locker!คริสตัลแดง') :
        getData = str(message.content)
        getDatatoNum = int(getData[17:])
        print('Locker Getting Data คริสตัลแดง from User is :',getDatatoNum,'Date :',day)
        readData = pd.read_excel('Locker.xlsx')
        print('กำลังอ่านข้อมูล...')
        callData = str(readData.iloc[12,0])
        print('ข้อมูลปัจจุบันที่อ่านได้คือ',callData)
        callDatatoNum = int(callData[11:])
        editTest = callDatatoNum + getDatatoNum
        editData = str('คริสตัลแดง_%d' %editTest)
        print('ข้อมูลหลังการคำนวณ',editTest)
        fixData = readData.replace([callData],[editData])
        writeData = pd.ExcelWriter('Locker.xlsx',engine='xlsxwriter')
        fixData.to_excel(writeData,index = False)
        writeData.save()
        
        readData = pd.read_excel('Locker.xlsx')
        callData = str(readData.iloc[12,0])
        print('ข้อมูลหลังการอัพเดท',callData)
        await message.channel.send('อัพเดทข้อมูลเสร็จสิ้น ตรวจสอบข้อมูลได้ที่ sb!Checklocker')
        print('การอัพเดทข้อมูล คริสตัลแดง เสร็จสิ้น!')

    #คริสตัลเงิน
    elif message.content.startswith('Locker!คริสตัลเงิน') :
        getData = str(message.content)
        getDatatoNum = int(getData[18:])
        print('Locker Getting Data คริสตัลเงิน from User is :',getDatatoNum,'Date :',day)
        readData = pd.read_excel('Locker.xlsx')
        print('กำลังอ่านข้อมูล...')
        callData = str(readData.iloc[13,0])
        print('ข้อมูลปัจจุบันที่อ่านได้คือ',callData)
        callDatatoNum = int(callData[12:])
        editTest = callDatatoNum + getDatatoNum
        editData = str('คริสตัลเงิน_%d' %editTest)
        print('ข้อมูลหลังการคำนวณ',editTest)
        fixData = readData.replace([callData],[editData])
        writeData = pd.ExcelWriter('Locker.xlsx',engine='xlsxwriter')
        fixData.to_excel(writeData,index = False)
        writeData.save()
        
        readData = pd.read_excel('Locker.xlsx')
        callData = str(readData.iloc[13,0])
        print('ข้อมูลหลังการอัพเดท',callData)
        await message.channel.send('อัพเดทข้อมูลเสร็จสิ้น ตรวจสอบข้อมูลได้ที่ sb!Checklocker')
        print('การอัพเดทข้อมูล คริสตัลเงิน เสร็จสิ้น!')

    #คริสตัลทอง
    elif message.content.startswith('Locker!คริสตัลทอง') :
        getData = str(message.content)
        getDatatoNum = int(getData[17:])
        print('Locker Getting Data คริสตัลทอง from User is :',getDatatoNum,'Date :',day)
        readData = pd.read_excel('Locker.xlsx')
        print('กำลังอ่านข้อมูล...')
        callData = str(readData.iloc[14,0])
        print('ข้อมูลปัจจุบันที่อ่านได้คือ',callData)
        callDatatoNum = int(callData[11:])
        editTest = callDatatoNum + getDatatoNum
        editData = str('คริสตัลทอง_%d' %editTest)
        print('ข้อมูลหลังการคำนวณ',editTest)
        fixData = readData.replace([callData],[editData])
        writeData = pd.ExcelWriter('Locker.xlsx',engine='xlsxwriter')
        fixData.to_excel(writeData,index = False)
        writeData.save()
        
        readData = pd.read_excel('Locker.xlsx')
        callData = str(readData.iloc[14,0])
        print('ข้อมูลหลังการอัพเดท',callData)
        await message.channel.send('อัพเดทข้อมูลเสร็จสิ้น ตรวจสอบข้อมูลได้ที่ sb!Checklocker')
        print('การอัพเดทข้อมูล คริสตัลทอง เสร็จสิ้น!')

    #เพชรฟ้า
    elif message.content.startswith('Locker!เพชรฟ้า') :
        getData = str(message.content)
        getDatatoNum = int(getData[14:])
        print('Locker Getting Data เพชรฟ้า from User is :',getDatatoNum,'Date :',day)
        readData = pd.read_excel('Locker.xlsx')
        print('กำลังอ่านข้อมูล...')
        callData = str(readData.iloc[15,0])
        print('ข้อมูลปัจจุบันที่อ่านได้คือ',callData)
        callDatatoNum = int(callData[8:])
        editTest = callDatatoNum + getDatatoNum
        editData = str('เพชรฟ้า_%d' %editTest)
        print('ข้อมูลหลังการคำนวณ',editTest)
        fixData = readData.replace([callData],[editData])
        writeData = pd.ExcelWriter('Locker.xlsx',engine='xlsxwriter')
        fixData.to_excel(writeData,index = False)
        writeData.save()
        
        readData = pd.read_excel('Locker.xlsx')
        callData = str(readData.iloc[15,0])
        print('ข้อมูลหลังการอัพเดท',callData)
        await message.channel.send('อัพเดทข้อมูลเสร็จสิ้น ตรวจสอบข้อมูลได้ที่ sb!Checklocker')
        print('การอัพเดทข้อมูล เพชรฟ้า เสร็จสิ้น!')

    #มันบด
    elif message.content.startswith('Locker!มันบด') :
        getData = str(message.content)
        getDatatoNum = int(getData[12:])
        print('Locker Getting Data มันบด from User is :',getDatatoNum,'Date :',day)
        readData = pd.read_excel('Locker.xlsx')
        print('กำลังอ่านข้อมูล...')
        callData = str(readData.iloc[16,0])
        print('ข้อมูลปัจจุบันที่อ่านได้คือ',callData)
        callDatatoNum = int(callData[6:])
        editTest = callDatatoNum + getDatatoNum
        editData = str('มันบด_%d' %editTest)
        print('ข้อมูลหลังการคำนวณ',editTest)
        fixData = readData.replace([callData],[editData])
        writeData = pd.ExcelWriter('Locker.xlsx',engine='xlsxwriter')
        fixData.to_excel(writeData,index = False)
        writeData.save()
        
        readData = pd.read_excel('Locker.xlsx')
        callData = str(readData.iloc[16,0])
        print('ข้อมูลหลังการอัพเดท',callData)
        await message.channel.send('อัพเดทข้อมูลเสร็จสิ้น ตรวจสอบข้อมูลได้ที่ sb!Checklocker')
        print('การอัพเดทข้อมูล มันบด เสร็จสิ้น!')

    #KFC
    elif message.content.startswith('Locker!KFC') :
        getData = str(message.content)
        getDatatoNum = int(getData[10:])
        print('Locker Getting Data KFC from User is :',getDatatoNum,'Date :',day)
        readData = pd.read_excel('Locker.xlsx')
        print('กำลังอ่านข้อมูล...')
        callData = str(readData.iloc[17,0])
        print('ข้อมูลปัจจุบันที่อ่านได้คือ',callData)
        callDatatoNum = int(callData[4:])
        editTest = callDatatoNum + getDatatoNum
        editData = str('KFC_%d' %editTest)
        print('ข้อมูลหลังการคำนวณ',editTest)
        fixData = readData.replace([callData],[editData])
        writeData = pd.ExcelWriter('Locker.xlsx',engine='xlsxwriter')
        fixData.to_excel(writeData,index = False)
        writeData.save()
        
        readData = pd.read_excel('Locker.xlsx')
        callData = str(readData.iloc[17,0])
        print('ข้อมูลหลังการอัพเดท',callData)
        await message.channel.send('อัพเดทข้อมูลเสร็จสิ้น ตรวจสอบข้อมูลได้ที่ sb!Checklocker')
        print('การอัพเดทข้อมูล KFC เสร็จสิ้น!')

    #เศษเหล็ก
    elif message.content.startswith('Locker!เศษเหล็ก') :
        getData = str(message.content)
        getDatatoNum = int(getData[15:])
        print('Locker Getting Data เศษเหล็ก from User is :',getDatatoNum,'Date :',day)
        readData = pd.read_excel('Locker.xlsx')
        print('กำลังอ่านข้อมูล...')
        callData = str(readData.iloc[18,0])
        print('ข้อมูลปัจจุบันที่อ่านได้คือ',callData)
        callDatatoNum = int(callData[9:])
        editTest = callDatatoNum + getDatatoNum
        editData = str('เศษเหล็ก_%d' %editTest)
        print('ข้อมูลหลังการคำนวณ',editTest)
        fixData = readData.replace([callData],[editData])
        writeData = pd.ExcelWriter('Locker.xlsx',engine='xlsxwriter')
        fixData.to_excel(writeData,index = False)
        writeData.save()
        
        readData = pd.read_excel('Locker.xlsx')
        callData = str(readData.iloc[18,0])
        print('ข้อมูลหลังการอัพเดท',callData)
        await message.channel.send('อัพเดทข้อมูลเสร็จสิ้น ตรวจสอบข้อมูลได้ที่ sb!Checklocker')
        print('การอัพเดทข้อมูล เศษเหล็ก เสร็จสิ้น!')

    #ไผ่
    elif message.content.startswith('Locker!ไผ่') :
        getData = str(message.content)
        getDatatoNum = int(getData[10:])
        print('Locker Getting Data ไผ่ from User is :',getDatatoNum,'Date :',day)
        readData = pd.read_excel('Locker.xlsx')
        print('กำลังอ่านข้อมูล...')
        callData = str(readData.iloc[19,0])
        print('ข้อมูลปัจจุบันที่อ่านได้คือ',callData)
        callDatatoNum = int(callData[4:])
        editTest = callDatatoNum + getDatatoNum
        editData = str('ไผ่_%d' %editTest)
        print('ข้อมูลหลังการคำนวณ',editTest)
        fixData = readData.replace([callData],[editData])
        writeData = pd.ExcelWriter('Locker.xlsx',engine='xlsxwriter')
        fixData.to_excel(writeData,index = False)
        writeData.save()
        
        readData = pd.read_excel('Locker.xlsx')
        callData = str(readData.iloc[19,0])
        print('ข้อมูลหลังการอัพเดท',callData)
        await message.channel.send('อัพเดทข้อมูลเสร็จสิ้น ตรวจสอบข้อมูลได้ที่ sb!Checklocker')
        print('การอัพเดทข้อมูล ไผ่ เสร็จสิ้น!')

    #น้ำกระบองเพชร
    elif message.content.startswith('Locker!น้ำกระบองเพชร') :
        getData = str(message.content)
        getDatatoNum = int(getData[20:])
        print('Locker Getting Data น้ำกระบองเพชร from User is :',getDatatoNum,'Date :',day)
        readData = pd.read_excel('Locker.xlsx')
        print('กำลังอ่านข้อมูล...')
        callData = str(readData.iloc[20,0])
        print('ข้อมูลปัจจุบันที่อ่านได้คือ',callData)
        callDatatoNum = int(callData[14:])
        editTest = callDatatoNum + getDatatoNum
        editData = str('น้ำกระบองเพชร_%d' %editTest)
        print('ข้อมูลหลังการคำนวณ',editTest)
        fixData = readData.replace([callData],[editData])
        writeData = pd.ExcelWriter('Locker.xlsx',engine='xlsxwriter')
        fixData.to_excel(writeData,index = False)
        writeData.save()
        
        readData = pd.read_excel('Locker.xlsx')
        callData = str(readData.iloc[20,0])
        print('ข้อมูลหลังการอัพเดท',callData)
        await message.channel.send('อัพเดทข้อมูลเสร็จสิ้น ตรวจสอบข้อมูลได้ที่ sb!Checklocker')
        print('การอัพเดทข้อมูล น้ำกระบองเพชร เสร็จสิ้น!')

    #ขวดเลือดซอมบี้
    elif message.content.startswith('Locker!ขวดเลือดซอมบี้') :
        getData = str(message.content)
        getDatatoNum = int(getData[21:])
        print('Locker Getting Data ขวดเลือดซอมบี้ from User is :',getDatatoNum,'Date :',day)
        readData = pd.read_excel('Locker.xlsx')
        print('กำลังอ่านข้อมูล...')
        callData = str(readData.iloc[21,0])
        print('ข้อมูลปัจจุบันที่อ่านได้คือ',callData)
        callDatatoNum = int(callData[15:])
        editTest = callDatatoNum + getDatatoNum
        editData = str('ขวดเลือดซอมบี้_%d' %editTest)
        print('ข้อมูลหลังการคำนวณ',editTest)
        fixData = readData.replace([callData],[editData])
        writeData = pd.ExcelWriter('Locker.xlsx',engine='xlsxwriter')
        fixData.to_excel(writeData,index = False)
        writeData.save()
        
        readData = pd.read_excel('Locker.xlsx')
        callData = str(readData.iloc[21,0])
        print('ข้อมูลหลังการอัพเดท',callData)
        await message.channel.send('อัพเดทข้อมูลเสร็จสิ้น ตรวจสอบข้อมูลได้ที่ sb!Checklocker')
        print('การอัพเดทข้อมูล ขวดเลือดซอมบี้ เสร็จสิ้น!')

    #เซรุ่มสกัด
    elif message.content.startswith('Locker!เซรุ่มสกัด') :
        getData = str(message.content)
        getDatatoNum = int(getData[17:])
        print('Locker Getting Data เซรุ่มสกัด from User is :',getDatatoNum,'Date :',day)
        readData = pd.read_excel('Locker.xlsx')
        print('กำลังอ่านข้อมูล...')
        callData = str(readData.iloc[22,0])
        print('ข้อมูลปัจจุบันที่อ่านได้คือ',callData)
        callDatatoNum = int(callData[11:])
        editTest = callDatatoNum + getDatatoNum
        editData = str('เซรุ่มสกัด_%d' %editTest)
        print('ข้อมูลหลังการคำนวณ',editTest)
        fixData = readData.replace([callData],[editData])
        writeData = pd.ExcelWriter('Locker.xlsx',engine='xlsxwriter')
        fixData.to_excel(writeData,index = False)
        writeData.save()
        
        readData = pd.read_excel('Locker.xlsx')
        callData = str(readData.iloc[22,0])
        print('ข้อมูลหลังการอัพเดท',callData)
        await message.channel.send('อัพเดทข้อมูลเสร็จสิ้น ตรวจสอบข้อมูลได้ที่ sb!Checklocker')
        print('การอัพเดทข้อมูล เซรุ่มสกัด เสร็จสิ้น!')

    #ระเบิดสตั้น
    elif message.content.startswith('Locker!ระเบิดสตั้น') :
        getData = str(message.content)
        getDatatoNum = int(getData[18:])
        print('Locker Getting Data ระเบิดสตั้น from User is :',getDatatoNum,'Date :',day)
        readData = pd.read_excel('Locker.xlsx')
        print('กำลังอ่านข้อมูล...')
        callData = str(readData.iloc[23,0])
        print('ข้อมูลปัจจุบันที่อ่านได้คือ',callData)
        callDatatoNum = int(callData[12:])
        editTest = callDatatoNum + getDatatoNum
        editData = str('ระเบิดสตั้น_%d' %editTest)
        print('ข้อมูลหลังการคำนวณ',editTest)
        fixData = readData.replace([callData],[editData])
        writeData = pd.ExcelWriter('Locker.xlsx',engine='xlsxwriter')
        fixData.to_excel(writeData,index = False)
        writeData.save()
        
        readData = pd.read_excel('Locker.xlsx')
        callData = str(readData.iloc[23,0])
        print('ข้อมูลหลังการอัพเดท',callData)
        await message.channel.send('อัพเดทข้อมูลเสร็จสิ้น ตรวจสอบข้อมูลได้ที่ sb!Checklocker')
        print('การอัพเดทข้อมูล ระเบิดสตั้น เสร็จสิ้น!')

    #เปล
    elif message.content.startswith('Locker!เปล') :
        getData = str(message.content)
        getDatatoNum = int(getData[10:])
        print('Locker Getting Data เปล from User is :',getDatatoNum,'Date :',day)
        readData = pd.read_excel('Locker.xlsx')
        print('กำลังอ่านข้อมูล...')
        callData = str(readData.iloc[24,0])
        print('ข้อมูลปัจจุบันที่อ่านได้คือ',callData)
        callDatatoNum = int(callData[4:])
        editTest = callDatatoNum + getDatatoNum
        editData = str('เปล_%d' %editTest)
        print('ข้อมูลหลังการคำนวณ',editTest)
        fixData = readData.replace([callData],[editData])
        writeData = pd.ExcelWriter('Locker.xlsx',engine='xlsxwriter')
        fixData.to_excel(writeData,index = False)
        writeData.save()
        
        readData = pd.read_excel('Locker.xlsx')
        callData = str(readData.iloc[24,0])
        print('ข้อมูลหลังการอัพเดท',callData)
        await message.channel.send('อัพเดทข้อมูลเสร็จสิ้น ตรวจสอบข้อมูลได้ที่ sb!Checklocker')
        print('การอัพเดทข้อมูล เปล เสร็จสิ้น!')

    #ไม้
    elif message.content.startswith('Locker!ไม้') :
        getData = str(message.content)
        getDatatoNum = int(getData[10:])
        print('Locker Getting Data ไม้ from User is :',getDatatoNum,'Date :',day)
        readData = pd.read_excel('Locker.xlsx')
        print('กำลังอ่านข้อมูล...')
        callData = str(readData.iloc[25,0])
        print('ข้อมูลปัจจุบันที่อ่านได้คือ',callData)
        callDatatoNum = int(callData[4:])
        editTest = callDatatoNum + getDatatoNum
        editData = str('ไม้_%d' %editTest)
        print('ข้อมูลหลังการคำนวณ',editTest)
        fixData = readData.replace([callData],[editData])
        writeData = pd.ExcelWriter('Locker.xlsx',engine='xlsxwriter')
        fixData.to_excel(writeData,index = False)
        writeData.save()
        
        readData = pd.read_excel('Locker.xlsx')
        callData = str(readData.iloc[25,0])
        print('ข้อมูลหลังการอัพเดท',callData)
        await message.channel.send('อัพเดทข้อมูลเสร็จสิ้น ตรวจสอบข้อมูลได้ที่ sb!Checklocker')
        print('การอัพเดทข้อมูล ไม้ เสร็จสิ้น!')

    #เศษไม้
    elif message.content.startswith('Locker!เศษไม้') :
        getData = str(message.content)
        getDatatoNum = int(getData[13:])
        print('Locker Getting Data เศษไม้ from User is :',getDatatoNum,'Date :',day)
        readData = pd.read_excel('Locker.xlsx')
        print('กำลังอ่านข้อมูล...')
        callData = str(readData.iloc[26,0])
        print('ข้อมูลปัจจุบันที่อ่านได้คือ',callData)
        callDatatoNum = int(callData[7:])
        editTest = callDatatoNum + getDatatoNum
        editData = str('เศษไม้_%d' %editTest)
        print('ข้อมูลหลังการคำนวณ',editTest)
        fixData = readData.replace([callData],[editData])
        writeData = pd.ExcelWriter('Locker.xlsx',engine='xlsxwriter')
        fixData.to_excel(writeData,index = False)
        writeData.save()
        
        readData = pd.read_excel('Locker.xlsx')
        callData = str(readData.iloc[26,0])
        print('ข้อมูลหลังการอัพเดท',callData)
        await message.channel.send('อัพเดทข้อมูลเสร็จสิ้น ตรวจสอบข้อมูลได้ที่ sb!Checklocker')
        print('การอัพเดทข้อมูล เศษไม้ เสร็จสิ้น!')

    '''#Test
    elif message.content.startswith('Locker!Test') :
        getData = str(message.content)
        getDatatoNum = int(getData[11:])
        print('Locker Getting Data Test from User is :',getDatatoNum,'Date :',day)
        readData = pd.read_excel('Locker.xlsx')
        print('กำลังอ่านข้อมูล...')
        Test = str(readData.iloc[18,0])
        print('ข้อมูลปัจจุบันที่อ่านได้คือ',Test)
        TesttoNum = int(Test[5:])
        editTest = TesttoNum + getDatatoNum
        editData = str('Test_%d' %editTest)
        print('ข้อมูลหลังการคำนวณ',editTest)
        fixData = readData.replace([Test],[editData])
        writeData = pd.ExcelWriter('Locker.xlsx',engine='xlsxwriter')
        fixData.to_excel(writeData,index = False)
        writeData.save()
        
        readData = pd.read_excel('Locker.xlsx')
        Test = str(readData.iloc[18,0])
        print('ข้อมูลหลังการอัพเดท',Test)
        await message.channel.send('อัพเดทข้อมูลเสร็จสิ้น ตรวจสอบข้อมูลได้ที่ sb!Checklocker')
        print('การอัพเดทข้อมูล Test เสร็จสิ้น!')'''

    #1
    if message.content == ('Checklist!Tori') :
        await message.channel.send('Name : Tori Charlotte >> Save Complete!')
        print('Tori',day)
        return tori()

    #2
    elif message.content == ('Checklist!Bella') :
        await message.channel.send('Name : Bella Rose >> Save Complete!')
        print('Bella',day)
        return bella()

    #3
    elif message.content == ('Checklist!White') :
        await message.channel.send('Name : White SB >> Save Complete!')
        print('White',day)
        return white()

    #4
    elif message.content == ('Checklist!Ozone') :
        await message.channel.send('Name : Ozone Binladen >> Save Complete!')
        print('Ozone',day)
        return ozone()

    #5
    elif message.content == ('Checklist!Run') :
        await message.channel.send('Name : Run MorningStar >> Save Complete!')
        print('Run',day)
        return run()

    #6
    elif message.content == ('Checklist!Somchai') :
        await message.channel.send('Name : Somchai Parangbai >> Save Complete!')
        print('Somchai',day)
        return somchai()

    #7
    elif message.content == ('Checklist!Lucino') :
        await message.channel.send('Name : Lucino Espresso >> Save Complete!')
        print('Lucino',day)
        return lucino()

    #8
    elif message.content == ('Checklist!Boy') :
        await message.channel.send('Name : Boy Butler >> Save Complete!')
        print('Boy',day)
        return boy()

    #9
    elif message.content == ('Checklist!Olym') :
        await message.channel.send('Name : Olym Binlahden >> Save Complete!')
        print('Olym',day)
        return olym()

    #10
    elif message.content == ('Checklist!Somtuy') :
        await message.channel.send('Name : Somtuy Serpent >> Save Complete!')
        print('Somtuy',day)
        return somtuy()

    #11
    elif message.content == ('Checklist!Tang') :
        await message.channel.send('Name : Tang Zii >> Save Complete!')
        print('Tang',day)
        return tang()

    #12
    elif message.content == ('Checklist!Kern') :
        await message.channel.send('Name : Bang Kern >> Save Complete!')
        print('Kern',day)
        return kern()

    #13
    elif message.content == ('Checklist!Somii') :
        await message.channel.send('Name : Somii Rose >> Save Complete!')
        print('Somii',day)
        return somii()

    #14
    elif message.content == ('Checklist!Somtui') :
        await message.channel.send('Name : Somtui Louisan >> Save Complete!')
        print('Somtui',day)
        return somtui()

    #15
    elif message.content == ('Checklist!GreenTea') :
        await message.channel.send('Name : GreenTea Xakos >> Save Complete!')
        print('GreenTea',day)
        return greentea()

    #16
    elif message.content == ('Checklist!Artee') :
        await message.channel.send('Name : Artee >> Save Complete!')
        print('Artee',day)
        return artee()

    #17
    elif message.content == ('Checklist!Es') :
        await message.channel.send('Name : Es Presso >> Save Complete!')
        print('Es',day)
        return es()

    #18
    elif message.content == ('Checklist!Bob') :
        await message.channel.send('Name : Bob Phranakhon >> Save Complete!')
        print('Bob',day)
        return bob()

    #19
    elif message.content == ('Checklist!Boi') :
        await message.channel.send('Name : Boi Phrankhon >> Save Complete!')
        print('Boi',day)
        return boi()

    #20
    elif message.content == ('Checklist!Chaom') :
        await message.channel.send('Name : Chaom Kan >> Save Complete!')
        print('Chaom',day)
        return chaom()

    #21
    elif message.content == ('Checklist!Mhok') :
        await message.channel.send('Name : Mhok Robinson >> Save Complete!')
        print('Mhok',day)
        return mhok()

    #22
    elif message.content == ('Checklist!David') :
        await message.channel.send('Name : David Namoys >> Save Complete!')
        print('David',day)
        return david()

    #23
    elif message.content == ('Checklist!Logan') :
        await message.channel.send('Name : Logan Cullen >> Save Complete!')
        print('Logan',day)
        return logan()

    #24
    elif message.content == ('Checklist!Bubee') :
        await message.channel.send('Name : Bubee Inboso >> Save Complete!')
        print('Bubee',day)
        return bubee()

    #25
    elif message.content == ('Checklist!Rojin') :
        await message.channel.send('Name : Rojin Black >> Save Complete!')
        print('Rojin',day)
        return rojin()

    #26
    elif message.content == ('Checklist!Haji') :
        await message.channel.send('Name : Haji City >> Save Complete!')
        print('Haji',day)
        return haji()

    #27
    elif message.content == ('Checklist!Ford') :
        await message.channel.send('Name : Ford Blacklist >> Save Complete!')
        print('Ford',day)
        return ford()

    #28
    elif message.content == ('Checklist!Shouta') :
        await message.channel.send('Name : Shouta Biggory >> Save Complete!')
        print('Shouta',day)
        return shouta()

    #29
    elif message.content == ('Checklist!Mica') :
        await message.channel.send('Name : Mica Black >> Save Complete!')
        print('Mica',day)
        return mica()

    #30
    elif message.content == ('Checklist!Mikey') :
        await message.channel.send('Name : Mikey Kung >> Save Complete!')
        print('Mikey',day)
        return mikey()

    #31
    elif message.content == ('Checklist!Mari') :
        await message.channel.send('Name : Mari Mala >> Save Complete!')
        print('Mari',day)
        return mari()

'''
@bot.command()
async def Test(ctx) :
    embed = discord.Embed(title = "SHELBY" , description = "Inprogress!\nComing Soon!!" , color=0x000000)
    embed.set_thumbnail(url = "https://media.discordapp.net/attachments/936369950686314579/952557305302511736/Logo_SB_SS4.png?width=472&height=472")
    await ctx.send(embed=embed)

@bot.command()
async def Help(ctx) :
    #await ctx.send('***การใช้งานบอท***\n\n- ใช้คำสั่งนำหน้า sb! ทุกครั้งเพื่อใช้งานบอทแล้วตัวแรกหลังเครื่องหมาย ! ต้องเป็นตัวพิมพ์ใหญ่เท่านั้น\n\nชุดคำสั่ง\n- การเช็คชื่อส่งของให้พิมพ์ sb! แล้วตามด้วยชื่อนำหน้าหรือเช็คได้ที่ sb!Slot\n- sb!Slot แสดงรายชื่อสล็อตแก๊ง\n- sb!Help เมนูช่วยเหลือ/แนะนำการใช้งาน\n- sb!Checklist เช็คข้อมูลในระบบ \n- sb!Checkdate เช็ควันที่ในระบบ')
    embed = discord.Embed(title = "SHELBY HELP" , description = "อยู่ในระหว่างการอัพเดท" , color=0x000000)
    embed.set_thumbnail(url = "https://media.discordapp.net/attachments/936369950686314579/952557305302511736/Logo_SB_SS4.png?width=472&height=472")
    await ctx.send(embed=embed)

@bot.command()
async def Slot(ctx) :
    embed = discord.Embed(title = "SHELBY SLOT" , description = "1. Tori Charlotte\n2. Bella Rose\n3. White SB\n4. Ozone Binladen\n5. Run MorningStar\n6. Somchai Parangbai\n7. Lucino Espresso\n8. Boy Butler\n9. Olym Binlahden\n10. Somtuy Serpent\n11. Tang Zii\n12. Bang Kern\n13. Somii Rose\n14. Somtui Louisan\n15. GreenTea Xakos\n16. Artee\n17. Es Presso\n18. Bob Phranakhon\n19. Boi Phrankhon\n20. Chaom Kan\n21. Mhok Robinson\n22. David Namoys\n23. Logan Cullen\n24. Bubee Inboso\n25. Rojin Black\n26. Haji City\n27. Ford Blacklist\n28. Shouta Biggory\n29. Mica Black\n30. Mikey Kung\n31. Mari Mala\n\nUpdate : 21/04/2565" , color=0x000000)
    embed.set_thumbnail(url = "https://media.discordapp.net/attachments/936369950686314579/952557305302511736/Logo_SB_SS4.png?width=472&height=472")
    await ctx.send(embed=embed)

@bot.command()
async def Checklist(ctx) :
    dataBase = pd.read_excel('Data.xlsx')
    embed = discord.Embed(title = "Checklist" , description = dataBase , color=0x000000)
    #embed.set_thumbnail(url = "https://media.discordapp.net/attachments/936369950686314579/952557305302511736/Logo_SB_SS4.png?width=472&height=472")
    await ctx.send(embed=embed)

@bot.command()
async def Checkdate(ctx) :
    await ctx.send(day)

@bot.command()
async def Callhistory10day(ctx) :
    History = pd.read_excel('ResultData.xlsx')
    embed = discord.Embed(title = "ยอดการส่งของ 10 ครั้งของวันที่ 12/04/65 - 21/04/65" , description = History , color=0x000000)
    #embed.set_thumbnail(url = "https://media.discordapp.net/attachments/936369950686314579/952557305302511736/Logo_SB_SS4.png?width=472&height=472")
    await ctx.send(embed=embed)

@bot.command()
async def Checklocker(ctx) :
    Locker = pd.read_excel('Locker.xlsx')
    embed = discord.Embed(title = "ตู้แก๊ง" , description = Locker , color=0x000000)
    #embed.set_thumbnail(url = "https://media.discordapp.net/attachments/936369950686314579/952557305302511736/Logo_SB_SS4.png?width=472&height=472")
    await ctx.send(embed=embed)

@bot.command()
async def Tori(ctx) :
    await ctx.send('Name : Tori Charlotte >> Save Complete!')
    print('Tori',day)
    return tori()

@bot.command()
async def Bella(ctx) :
    await ctx.send('Name : Bella Rose >> Save Complete!')
    print('Bella',day)
    return bella()

@bot.command()
async def White(ctx) :
    await ctx.send('Name : White SB >> Save Complete!')
    print('White',day)
    return white()

@bot.command()
async def Ozone(ctx) :
    await ctx.send('Name : Ozone Binladen >> Save Complete!')
    print('Ozone',day)
    return ozone()

@bot.command()
async def Run(ctx) :
    await ctx.send('Name : Run MorningStar >> Save Complete!')
    print('Run',day)
    return run()

@bot.command()
async def Somchai(ctx) :
    await ctx.send('Name : Somchai Parangbai >> Save Complete!')
    print('Somchai',day)
    return somchai()

@bot.command()
async def Lucino(ctx) :
    await ctx.send('Name : Lucino Espresso >> Save Complete!')
    print('Lucino',day)
    return lucino()

@bot.command()
async def Boy(ctx) :
    await ctx.send('Name : Boy Butler >> Save Complete!')
    print('Boy',day)
    return boy()

@bot.command()
async def Olym(ctx) :
    await ctx.send('Name : Olym Binlahden >> Save Complete!')
    print('Olym',day)
    return olym()

@bot.command()
async def Somtuy(ctx) :
    await ctx.send('Name : Somtuy Serpent >> Save Complete!')
    print('Somtuy',day)
    return somtuy()

@bot.command()
async def Tang(ctx) :
    await ctx.send('Name : Tang Zii >> Save Complete!')
    print('Tang',day)
    return tang()

@bot.command()
async def Kern(ctx) :
    await ctx.send('Name : Bang Kern >> Save Complete!')
    print('Kern',day)
    return kern()

@bot.command()
async def Somii(ctx) :
    await ctx.send('Name : Somii Rose >> Save Complete!')
    print('Somii',day)
    return somii()

@bot.command()
async def Somtui(ctx) :
    await ctx.send('Name : Somtui Louisan >> Save Complete!')
    print('Somtui',day)
    return somtui()

@bot.command()
async def GreenTea(ctx) :
    await ctx.send('Name : GreenTea Xakos >> Save Complete!')
    print('GreenTea',day)
    return greentea()

@bot.command()
async def Artee(ctx) :
    await ctx.send('Name : Artee >> Save Complete!')
    print('Artee',day)
    return artee()

@bot.command()
async def Es(ctx) :
    await ctx.send('Name : Es Presso >> Save Complete!')
    print('Es',day)
    return es()

@bot.command()
async def Bob(ctx) :
    await ctx.send('Name : Bob Phranakhon >> Save Complete!')
    print('Bob',day)
    return bob()

@bot.command()
async def Boi(ctx) :
    await ctx.send('Name : Boi Phrankhon >> Save Complete!')
    print('Boi',day)
    return boi()

@bot.command()
async def Chaom(ctx) :
    await ctx.send('Name : Chaom Kan >> Save Complete!')
    print('Chaom',day)
    return chaom()

@bot.command()
async def Mhok(ctx) :
    await ctx.send('Name : Mhok Robinson >> Save Complete!')
    print('Mhok',day)
    return mhok()

@bot.command()
async def David(ctx) :
    await ctx.send('Name : David Namoys >> Save Complete!')
    print('David',day)
    return david()

@bot.command()
async def Logan(ctx) :
    await ctx.send('Name : Logan Cullen >> Save Complete!')
    print('Logan',day)
    return logan()

@bot.command()
async def Bubee(ctx) :
    await ctx.send('Name : Bubee Inboso >> Save Complete!')
    print('Bubee',day)
    return bubee()

@bot.command()
async def Rojin(ctx) :
    await ctx.send('Name : Rojin Black >> Save Complete!')
    print('Rojin',day)
    return rojin()

@bot.command()
async def Haji(ctx) :
    await ctx.send('Name : Haji City >> Save Complete!')
    print('Haji',day)
    return haji()

@bot.command()
async def Ford(ctx) :
    await ctx.send('Name : Ford Blacklist >> Save Complete!')
    print('Ford',day)
    return ford()

@bot.command()
async def Shouta(ctx) :
    await ctx.send('Name : Shouta Biggory >> Save Complete!')
    print('Shouta',day)
    return shouta()

@bot.command()
async def Mica(ctx) :
    await ctx.send('Name : Mica Black >> Save Complete!')
    print('Mica',day)
    return mica()

@bot.command()
async def Mikey(ctx) :
    await ctx.send('Name : Mikey Kung >> Save Complete!')
    print('Mikey',day)
    return mikey()

@bot.command()
async def Mari(ctx) :
    await ctx.send('Name : Mari Mala >> Save Complete!')
    print('Mari',day)
    return mari()
'''

'''
@bot.event
async def on_message(message) :
    if message.content.startswith('Somchai') :
        await message.channel.send('Save Complete!')
'''
'''
@bot.event
async def on_message(message) :
    await bot.process_commands(message)

@bot.command()
async def test(ctx) :
    await ctx.send('Test!!')

@bot.command()
async def Mari(ctx) :
    await ctx.send('Mari Mala!!')
'''
'''
@bot.event
async def on_message(message) : #ดักรอข้อความใน Chat
    if message.content.startswith('?>ping') : #เมื่อข้อความในตัวแรกมีคำว่า ping
       await message.channel.send('Test BOT!') #ข้อความที่ต้องการตอบกลับ
'''
       
bot.run('')
