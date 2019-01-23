# id - 537560577870921758
# Token - NTM3NTYwNTc3ODcwOTIxNzU4.DynCSg.rHxQIv-FNrum6g9CIJyc9XsZAR0
# Permissions integer - 370688
# https://discordapp.com/oauth2/authorize?client_id=537560577870921758&scope=bot&permissions=370688

import discord
from discord import File
import time
from datetime import datetime as dt
import asyncio #todo async in its sleep as well
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")

client = discord.Client() #create client object

def report(guild):
    online = 0
    idle = 0
    offline = 0

    for m in guild.members:
        if str(m.status) is "online":
            online+=1
        elif str(m.status) is "offline":
            offline+=1
        else:
            idle+=1
    return online, offline, idle

async def user_metrics_bkgnd_task():
    await client.wait_until_ready()
    global my_guild
    my_guild = client.get_guild(532130189346340877)
    while not client.is_closed():
        try:
            online, offline, idle = report(my_guild)
            with open("user_metrics.csv", "a") as f:
                f.write(f"{dt.now().strftime('%H:%M:%S')}, {online}, {offline}, {idle}\n")


            df = pd.read_csv("user_metrics.csv", names=['time', 'online', 'offline', 'idle']) #assign column names
            df['total'] = df['online'] + df['offline'] + df['idle']
            df.drop("time", 1, inplace = True) #remove date time column

            plt.clf() #clear figure

            df['online'].plot()
            plt.legend()
            plt.savefig("graph.png")

            await asyncio.sleep(5)

        except Exception as err:
            print(str(err))
            await asyncio.sleep(5)

@client.event # event wrapper/decorator
async def on_ready(): #called one time when bot is conn to actual server
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    # global my_guild
    print(f"{message.channel}: {message.author.name}: {message.content}")

    if "hello" in message.content.lower(): #lower case
        await message.channel.send("Hey man!")

    elif "bye" in message.content.lower():
        await message.channel.send('ok :(')
        await client.close()

    #info about guild/server:
    elif "member count" in message.content.lower():
        await message.channel.send(f"```py\n{my_guild.member_count}```")
    
    elif "report" in message.content.lower():
        online, offline, idle = report(my_guild)
        await message.channel.send(f"```py\nOnline: {online}. \nIdle/busy/dnd: {idle}. \nOffline: {offline}```")
        file = File("graph.png", filename="graph.png")
        await message.channel.send("graph.png", file=file)

client.loop.create_task(user_metrics_bkgnd_task())
client.run("NTM3NTYwNTc3ODcwOTIxNzU4.DynCSg.rHxQIv-FNrum6g9CIJyc9XsZAR0")