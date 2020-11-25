#!/usr/bin/env python3
import discord
import time
import random
import serial

ser = serial.Serial('/dev/ttyS0', 9600)

client = discord.Client()

nds = 0
do = ""
common_sense_count = 0
sense_arr = []
light = ""

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
    global nds
    global do
    global common_sense_count
    global sense_arr
    global light
    if message.author.bot:
        return


    wordlist = open("/root/Bot/talk.txt", 'r')
    words = wordlist.readlines()
    wordlist.close()
    for word in words:
        word_split = word.split('%')
        input_word = word_split[0]
        output_word = word_split[1]
        output_file = word_split[2]
        if str(input_word) in message.content:
            if output_file == "f\n":
                await message.channel.send(file=discord.File(output_word))
            else:
                await message.channel.send(output_word)

    common_sense_count += 1
    if common_sense_count >= 10000 or ("시현아" in message.content and "상식" in message.content):
        common_sense_count = 0
        with open("/root/Bot/common_sense.txt", 'r') as common_sense:
            senses = common_sense.readlines()
            sense_num = random.randrange(len(senses))
            while sense_num in sense_arr:
                if len(sense_arr) == len(senses):
                    sense_arr = []
                    break
                sense_num = random.randrange(len(senses))
                if sense_num not in sense_arr:
                    break
        sense_arr.append(sense_num)
        sense = "그거알아?\n" + senses[sense_num]
        await message.channel.send(sense)

    if nds == 1:
        
    
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
                    if black_st <= black_st2 and int(black_st2 - black_st) <= 5:
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
                    if white_st <= white_st2 and int(white_st2 - white_st) <= 3:
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
                        if black_st <= black_st2 and int(black_st2 - black_st) <= 5:
                            black_st = black_st2
                            black_out += 1
                
                if black_out == len(blackword):
                    black = 1


            if black == 0:
                try:
                    await message.channel.send(message_)
                    await message.delete()
                except:
                    await message.channel.send('뭐라는겨')
            else:
                await message.channel.send('ㅇㅇㄴㅇ')
                black = 0
        else:
            wordlist = open("/root/Bot/prefix_talk.txt", 'r')
            words = wordlist.readlines()
            wordlist.close()
            for word in words:
                word_split = word.split('%')
                input_word = word_split[0]
                output_word = word_split[1]
                output_file = word_split[2]
                if str(input_word) in message.content:
                    if output_file == "f\n":
                        await message.channel.send(file=discord.File(output_word))
                    else:
                        await message.channel.send(output_word)

            if "wildcard" in str(message.mentions) or "sihyun_m00n" in str(message.mentions):
                await message.channel.send('왜')
                

            if "라고 말하면 안돼" in message.content or "라고 하면 안돼" in message.content:
                if message.author.id == 536932662972252170:
                    contrast = 0
                    inpuT = message.content.split()
                    i = inpuT.index("안돼")
                    i  = i - 3
                    blackword = inpuT[i]
                    blacklist = open('/root/Bot/dont_speak.txt', 'r')
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
                    elif whiteword != "시현아" and whiteword != "":
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
                    else:
                        await message.channel.send('뭐라는겨')
                else:
                    await message.channel.send('시룬데><')

            if "ㄴㄷㅆ" in message.content:
                nds = 1
                await message.channel.send('ㄴㄷㅆ??(각성)')
            if "미안해" in message.content or "진정" in message.content:
                nds = 0
                await message.channel.send('알았어...(진정)')


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
                if do == "":
                    if int(like(message.author.id)) >= 100:
                        await message.channel.send('니생각')
                    elif int(like(message.author.id)) >= 50:
                        await message.channel.send('"당신과함께"하는중,엌ㅋㅋㅋ')
                    elif int(like(message.author.id)) >= 20:
                        await message.channel.send('그냥? 암것도')
                    else:
                        await message.channel.send('알아서 뭐하게;')
                else:
                    await message.channel.send(do + '하는중')
                    
            elif "해" in message.content:
                if message.author.id == 536932662972252170:
                    try:
                        do = ""
                        inpuT = message.content.split()
                        end = inpuT.index("해")
                        start = inpuT.index("시현아")
                        start += 1
                        inpuT = inpuT[start:end]
                        for i in inpuT:
                            do = do + i + " "
                        if do == "":
                            await message.channel.send('뭐라는겨')
                        else:
                            await client.change_presence(activity = discord.Game(do))
                            await message.channel.send('알았어')
                    except:
                        await message.channel.send('뭐라는겨')
                else:
                    await message.channel.send('시룬데><')

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
                string = "시현아 ~ 라고 말해봐: 시현이가 말을합니다.\n시현아 안녕: 시현이가 인사합니다.\n시현아 내 호감도는?: 당신의 호감도를 알려줍니다.(시현이에게 욕을하면 호감도가 감소하고 좋은말을 해주면호감도가 증가합니다.)\n시현아 ~ (더하기/뺴기/곱하기/나누기) ~ 은?:사칙연산을합니다.\n시현아ㄴㄷㅆ:각성합니다.(하지마세요)\n시현아미안해:각성이풀립니다."
                await message.channel.send(string)

            if "불" in message.content:
                if "켜" in message.content:
                    if message.author.id == 536932662972252170:
                        light = "1"
                        await message.channel.send('알았어')
                    else:
                        await message.channel.send('시룬데><')
                elif "꺼" in message.content:
                    if message.author.id == 536932662972252170:
                        light = "0"
                        await message.channel.send('알았어')
                    else:
                        await message.channel.send('시룬데><')
                ser.write(light.encode())
                light = ""

with open("/root/Bot/sihyun_m00n-Token.txt", 'r') as token:
    client.run(token.read())
