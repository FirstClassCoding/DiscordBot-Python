import discord
from discord.ext import commands
from getTime import getTime

day = getTime('date')

bot = commands.Bot(command_prefix='!')
#กำหนด Prefix

@bot.event
async def on_ready() : #เมื่อระบบพร้อมใช้งาน
    print("Middle Craft Bot Started!\nDay : %s"%day) #แสดงผลใน CMD

@bot.event
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

    def Post():
        bot.loop.create_task(sendPost())

    async def sendPost():
        await bot.wait_until_ready()
        roomID = 973735912011870249
        pos = ['1. หมา 1 : ไฮเปอร์',
                '2. หมา 2 : เฟิร์ส',
                '3. คาวหน้า : เมนนิ',
                '4. คาวหลัง : เพชร',
                '5. แกะหน้า : โอ๊ต',
                '6. แกะหลัง : ',
                '7. เพนกวิ้น : เบ้น',
                '8. แมวปืน : ',
                '9. ต่ายหลัก : มาร์ช',
                '10. วาฬ : คูณ']
        text1 = 'อารีน่าเริ่ม 22.00- 23.00 เจอดิส 21:40'
        alltext = ''
        for i in range (0,10):
            alltext += pos[i] + '\n'
        alltext += text1
        embed = discord.Embed(title = 'VictoryBridge 10-10' , description = alltext , color = 0x000000)
        channel = bot.get_channel(roomID)
        await channel.send(embed=embed)

    command_text = str(input('Enter Passtext Here : '))

    if command_text.upper() == 'POST':
        command_text = ''
        return Post()


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

bot.run('')
