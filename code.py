# id - 537560577870921758
# Token - NTM3NTYwNTc3ODcwOTIxNzU4.DynCSg.rHxQIv-FNrum6g9CIJyc9XsZAR0
# Permissions integer - 370688
# https://discordapp.com/oauth2/authorize?client_id=537560577870921758&scope=bot&permissions=370688

import discord
import sys

client = discord.Client()

@client.event # event wrapper/decorator
async def on_ready(): #called one time when bot is conn to actual server
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author.name}: {message.content}")
    my_guild = client.get_guild(532130189346340877)

    if "hello" in message.content.lower(): #lower case
        await message.channel.send("Hey man!")

    elif "bye" in message.content.lower():
        await message.channel.send('ok :(')
        await client.close()
        sys.exit()

    #info about guild/server:
    elif "member count" in message.content.lower():
        await message.channel.send(f"```py\n{my_guild.member_count}```")
    
    elif "report" in message.content.lower():
        online = 0
        idle = 0
        offline = 0

        for m in my_guild.members:
            if str(m.status) is "online":
                online+=1
            elif str(m.status) is "offline":
                offline+=1
            else:
                idle+=1
        
        await message.channel.send(f"```Online: {online}. \nIdle/busy/dnd: {idle}. \nOffline: {offline}```")
client.run("NTM3NTYwNTc3ODcwOTIxNzU4.DynCSg.rHxQIv-FNrum6g9CIJyc9XsZAR0")