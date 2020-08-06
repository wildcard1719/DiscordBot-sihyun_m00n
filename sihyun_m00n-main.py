#!/usr/bin/env python3
import discord
import time

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "wildcard" in str(message.mentions) or "sihyun_m00n" in str(message.mentions):
        await message.channel.send('왜')

    if "시현아" in message.content:
        black = 0
        blacklist = open("/root/Bot/blacklist.txt", 'r')
        blackwords = blacklist.readlines()
        blacklist.close()
        for blackword in blackwords:
            black_out = 0
            black_st = 0
            black_st2 = 0
            blackword = blackword[:-1]
            for blackchar in blackword:
                if blackchar in message.content[4:]:
                    black_st2 = message.content[4:].index(blackchar)
                    if black_st <= black_st2:
                        black_st = black_st2
                        black_out += 1

            if black_out == len(blackword):
                black = 1
            
        if black == 1:
            await message.channel.send(file=discord.File('/home/pi/DiscordBot-sihyun_m00n/pics/fuckyou.jpg'))
            await message.channel.send(message.author.id)
            black = 0

   
        if "라고 말해봐" in message.content:
            black = 0
            message_ = ""
            inpuT = message.content.split()
            st = inpuT.index("시현아")
            i = inpuT.index("말해봐")
            i = i - 1
            st = st + 1
            for message__ in inpuT[st:i]:
                message_ = message_ + message__ + " "

            blacklist = open("/root/Bot/blacklist.txt", 'r')
            blackwords = blacklist.readlines()
            blacklist.close()
            for blackword in blackwords:
                black_out = 0
                black_st = 0
                black_st2 = 0
                blackword = blackword[:-1]
                lenth = len(blackword)
                for blackchar in blackword:
                    if blackchar in message_:
                        black_st2 = message_.index(blackchar)
                        if black_st <= black_st2:
                            black_st = black_st2
                            black_out += 1
                
                if black_out == len(blackword):
                    black = 1


            if black == 0:
                await message.channel.send(message_)
            else:
                await message.channel.send('ㅇㅇㄴㅇ')
                black = 0
        else:    

            if "라고 말하면 안돼" in message.content or "라고 하면 안돼" in message.content:
                if message.author.id == 536932662972252170:
                    inpuT = message.content.split()
                    i = inpuT.index("안돼")
                    i  = i - 3
                    blackword = inpuT[i]
                    with open("/root/Bot/blacklist.txt", 'a') as blacklist:
                        blacklist.write(blackword + "\n")
                    await message.channel.send('알았어')
                else:
                    await message.channel.send('시룬데><')


            if "안녕" in message.content or "하이" in message.content:
                await message.channel.send('안녕?')
        
            if "잘지내" in message.content or "잘있어" in message.content:
                if '?' in message.content:
                    await message.channel.send('나야 잘지내지')
                else:
                    if "난" in message.content or "나" in message.content:
                        await message.channel.send('잘지낸다니 다행이네')
                    else:
                        await message.channel.send('어디가?')
     

            if "심심" in message.content:
                if "?" in message.content:
                    await message.channel.send('딱히? ')
                else:
                    await message.channel.send('아르마해,아르마')

            if "불 좀 꺼줄래" in message.content:
                await message.channel.send('니 삼성램이잖아')

            if "인성문제" in message.content:
                await message.channel.send('아..아닙니다!')
        
            if "자기소개" in message.content:
                if "지마" in message.content:
                    await message.channel.send('할껀데?')
                    time.sleep(1)
                await message.channel.send('이름:문시현\n나이:17세\n키:170cm \n몸무게:62kg\n좋아하는것:오코노미야끼,전기전자,컴퓨터,코딩,드론,DIY등등\n싫어하는것:큰거미,안큰거미')
        
            if "몇시" in message.content:
                now = time.localtime(time.time())
                hour = now.tm_hour
                if hour >= 13:
                    hour -= 12
                await message.channel.send(str(hour) + "시" + str(now.tm_min) + "분이야")

            if "드론" in message.content:
                await message.channel.send(file=discord.File('/home/pi/DiscordBot-sihyun_m00n/pics/dronefall.gif'))
            

            if "더하기" in message.content:
                try:
                    inpuT = message.content.split()
                    i = inpuT.index("더하기")
                    i = i - 1
                    number1 = inpuT[i]
                    i = i + 2
                    number2 = inpuT[i]
                    result = float(number1) + float(number2)
                    await message.channel.send(str(result))
                except:
                    await message.channel.send('뭐라는겨')

            if "빼기" in message.content:
                try:
                    inpuT = message.content.split()
                    i = inpuT.index("빼기")
                    i = i - 1
                    number1 = inpuT[i]
                    i = i + 2
                    number2 = inpuT[i]
                    result = float(number1) - float(number2)
                    await message.channel.send(str(result))
                except:
                    await message.channel.send('뭐라는겨')

            if "곱하기" in message.content:
                try:
                    inpuT = message.content.split()
                    i = inpuT.index("곱하기")
                    i = i - 1
                    number1 = inpuT[i]
                    i = i + 2
                    number2 = inpuT[i]
                    result = float(number1) * float(number2)
                    await message.channel.send(str(result))
                except:
                    await message.channel.send('뭐라는겨')

            if "나누기" in message.content:
                try:
                    inpuT = message.content.split()
                    i = inpuT.index("나누기")
                    i = i - 1
                    number1 = inpuT[i]
                    i = i + 2
                    number2 = inpuT[i]
                    result = float(number1) / float(number2)
                    await message.channel.send(str(result))
                except:
                    await message.channel.send('뭐라는겨')




with open("/root/Bot/sihyun_m00n-Token.txt", 'r') as token:
    client.run(token.read())
