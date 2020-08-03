import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if "시현아" in message.content:
        if "안녕" in message.content:
            await message.channel.send('안녕?')
        if "잘지내" in message.content or "잘있어" in message.content:
            if '?' in message.content:
                await message.channel.send('나야 잘지내지')
            else:
                if "난" in message.content:
                    await message.channel.send('잘지낸다니 다행이네')
                else:
                    await message.channel.send('어디가?')

with open("/root/Bot/sihyun_m00n-Token.txt", 'r') as token:
    client.run(token.read())
