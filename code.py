# id - 532127546226114563
# token - NTMyMTI3NTQ2MjI2MTE0NTYz.DxX-oQ.zdHB0JS9Mk5dPDsHRBSeZoD4gyk
# permissions integer - 67648

# https://discordapp.com/oauth2/authorize?client_id=532127546226114563&scope=bot&permissions=67648

import discord 

client = discord.Client()

@client.event #event decorator
async def on_ready(): #called one time when bot is connected to server
    print(f"Logged in as {client.user}")

client.run("NTMyMTI3NTQ2MjI2MTE0NTYz.DxX-oQ.zdHB0JS9Mk5dPDsHRBSeZoD4gyk")