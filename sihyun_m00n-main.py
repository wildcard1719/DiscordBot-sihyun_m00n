#!/usr/bin/env python3
import discord
import time
import random

client = discord.Client()

def replace_line(file_name, line_num, text):
    lines = open(file_name,'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

def like(id_: str):
    userlist = open("/root/Bot/userlist.txt", 'r')
    user_infos = userlist.readlines()
    for user_info in user_infos:
        if str(id_) in user_info:
            like_ = user_info.split()[1]
            break
    return like_

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "wildcard" in str(message.mentions) or "sihyun_m00n" in str(message.mentions):
        await message.channel.send('왜')
    if "ㅇㅅㅇ" in message.content:
        await message.channel.send('ㅇㅅㅇ')

    if "시현아" in message.content:
        black = 0
        white = 0

        user_in_list = 0
        userlist = open("/root/Bot/userlist.txt", 'r')
        user_infos = userlist.readlines()
        userlist.close()
        for user_info in user_infos:
            user_info = user_info[:-1]
            if str(message.author.id) in user_info:
                user_in_list = 1
        if user_in_list == 0:                
            with open("/root/Bot/userlist.txt", 'a') as userlist:
                userlist.write(str(message.author.id) + " 50\n")
        
        blacklist = open("/root/Bot/blackword.txt", 'r')
        blackwords = blacklist.readlines()
        blacklist.close()
        for blackword in blackwords:
            black_out = 0
            black_st = 0
            black_st2 = 0
            blackword = blackword[:-1]
            if blackword == "":
                continue
            for blackchar in blackword:
                if blackchar in message.content[4:]:
                    black_st2 = message.content[4:].index(blackchar)
                    if black_st <= black_st2:
                        black_st = black_st2
                        black_out += 1
            if black_out == len(blackword):
                black = 1

        whitelist = open("/root/Bot/whiteword.txt", 'r')
        whitewords = whitelist.readlines()
        whitelist.close()
        for whiteword in whitewords:
            white_out = 0
            white_st = 0
            white_st2 = 0
            whiteword = whiteword[:-1]
            if whiteword == "":
                continue
            for whitechar in whiteword:
                if whitechar in message.content[4:]:
                    white_st2 = message.content[4:].index(whitechar)
                    if white_st <= white_st2:
                        white_st = white_st2
                        white_out += 1
            if white_out == len(whiteword):
                white = 1
        
        userlist = open("/root/Bot/userlist.txt", 'r')
        user_infos = userlist.readlines()
        userlist.close()
        for user_info in user_infos:
            user_info = user_info[:-1]
            if str(message.author.id) in user_info:
                this_info = user_info
                this_id = user_info.split()[0]
                this_int = user_info.split()[1]
                if black == 1:
                    edit_line = this_id + " " + str(int(this_int) - random.randint(1, 3)) + "\n"
                    await message.channel.send(':(')
                elif white == 1:
                    edit_line = this_id + " " + str(int(this_int) + random.randint(1, 3)) + "\n"
                    await message.channel.send(':)')
                else:
                    edit_line = this_id + " " + this_int + "\n"
                replace_line("/root/Bot/userlist.txt", user_infos.index(this_info + "\n"), edit_line)

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

            blacklist = open("/root/Bot/dont_speak.txt", 'r')
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
                try:
                    await message.channel.send(message_)
                except:
                    await message.channel.send('뭐라는겨')
            else:
                await message.channel.send('ㅇㅇㄴㅇ')
                black = 0
        else:    

            if "라고 말하면 안돼" in message.content or "라고 하면 안돼" in message.content:
                if message.author.id == 536932662972252170:
                    contrast = 0
                    inpuT = message.content.split()
                    i = inpuT.index("안돼")
                    i  = i - 3
                    blackword = inpuT[i]
                    blacklist = open("/root/Bot/dont_speak.txt", 'r')
                    blackwords = blacklist.readlines()
                    blacklist.close()
                    for blackword_contrast in blackwords:
                        blackword_contrast = blackword_contrast[:-1]
                        if blackword == blackword_contrast:
                            contrast = 1
                    if contrast == 1:
                        await message.channel.send('나도알아')
                    elif blackword != "시현아" and blackword != "":
                        with open("/root/Bot/dont_speak.txt", 'a') as blacklist:
                            blacklist.write(blackword + "\n")
                        await message.channel.send('알았어')
                    else:
                        await message.channel.send('뭐라는겨')
                else:
                    await message.channel.send('시룬데><')

            if "은 좋은말이야" in message.content or "는 좋은말이야" in message.content:
                if message.author.id == 536932662972252170:
                    contrast = 0
                    inpuT = message.content.split()
                    i = inpuT.index("좋은말이야")
                    i  = i - 1
                    whiteword = inpuT[i]
                    whiteword = whiteword[:-1]
                    whitelist = open("/root/Bot/whiteword.txt", 'r')
                    whitewords = whitelist.readlines()
                    whitelist.close()
                    for whiteword_contrast in whitewords:
                        whiteword_contrast = whiteword_contrast[:-1]
                        if whiteword == whiteword_contrast:
                            contrast = 1
                    if contrast == 1:
                        await message.channel.send('나도알아')
                    elif blackword != "시현아" and blackword != "":
                        with open("/root/Bot/whiteword.txt", 'a') as whitelist:
                            whitelist.write(whiteword + "\n")
                        await message.channel.send('알았어')
                    else:
                        await message.channel.send('뭐라는겨')
                else:
                    await message.channel.send('시룬데><')
            


            if "은 나쁜말이야" in message.content or "는 나쁜말이야" in message.content:
                if message.author.id == 536932662972252170:
                    contrast = 0
                    inpuT = message.content.split()
                    i = inpuT.index("나쁜말이야")
                    i  = i - 1
                    blackword = inpuT[i]
                    blackword = blackword[:-1]
                    blacklist = open("/root/Bot/blackword.txt", 'r')
                    blackwords = blacklist.readlines()
                    blacklist.close()
                    for blackword_contrast in blackwords:
                        blackword_contrast = blackword_contrast[:-1]
                        if blackword == blackword_contrast:
                            contrast = 1
                    if contrast == 1:
                        await message.channel.send('나도알아')
                    elif blackword != "시현아" and blackword != "":
                        with open("/root/Bot/blackword.txt", 'a') as blacklist:
                            blacklist.write(blackword + "\n")
                        await message.channel.send('알았어')
                    else await message.channel.send('뭐라는겨')
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

            if "인성문제" in message.content or "인성 문제" in message.content:
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

            if "호감도" in message.content:
                try:
                    if "내" in message.content:
                        await message.channel.send(like(message.author.id) + "쯤?")
                    else:
                        mention = message.mentions
                        mention = str(mention).split()
                        word = mention[1]
                        id_ = word[3:]
                        if message.author.id == 536932662972252170:
                            await message.channel.send(like(id_) + "쯤?")
                        else :
                            if int(like(message.author.id)) >= 21:
                                await message.channel.send('안알려줄건데?')
                            else:
                                await message.channel.send('ㄲㅈ')
                except:
                    await message.channel.send('그런사람 모르는데?')
            
            if "뭐해" in message.content:
                if int(like(message.author.id)) >= 100:
                    await message.channel.send('니생각')
                elif int(like(message.author.id)) >= 50:
                    await message.channel.send('"당신과함께"하는중,엌ㅋㅋㅋ')
                elif int(like(message.author.id)) >= 20:
                    await message.channel.send('그냥? 암것도')
                else:
                    await message.channel.send('알아서 뭐하게;')
            
            if "지건" in message.content:
                await message.channel.send('딱대^^ㅣ바')

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

            if "도와줘" in message.content or "help" in message.content:
                string = "시현아 ~ 라고 말해봐: 시현이가 말을합니다.\n시현아 안녕: 시현이가 인사합니다.\n시현아 내 호감도는?: 당신의 호감도를 알려줍니다.(시현이에게 욕을하면 호감도가 감소하고 좋은말을 해주면호감도가 증가합니다.)\n시현아 몇시야?: 몇시인지 알려줍니다.\n시현아 ~ (더하기/뺴기/곱하기/나누기) ~ 은?:사칙연산을합니다."
                await message.channel.send(string)
                


with open("/root/Bot/sihyun_m00n-Token.txt", 'r') as token:
    client.run(token.read())
