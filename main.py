import os
import time
import discord
from filtered import filt
from alive import keepAlive

client = discord.Client()

@client.event
async def on_ready():
    print('ready to catch some bad kids!!!!')
    print(client.user)

@client.event
async def on_message(message):
    if message.author != client.user:
      filtered = filt(str(message.content).lower())
      if filtered[0] == True:
        if os.path.exists(str(message.author)+'.txt'):
          file1 = open(str(message.author)+'.txt','r').read()
          file2 = open(str(message.author)+'.txt','w')

          data = file1

          file2.write(str(int(file1) + 1))
          file2.close()
        else:
          file1 = open(str(message.author)+'.txt','w')
          file1.write('1')

        embed = discord.Embed(title = '⚠️ **Blacklisted word detected ⚠️**', 
        description = '**Message:**\n```'+str(message.content)+'```\n**Word Detected:**\n```'+filtered[1]+'```\n**Warning #:** '+str(int(data)+1),
        color = 0xe74c3c)
        time.sleep(0.5)
        await message.delete()
        await message.author.send(embed = embed)


keepAlive()
token = os.environ.get("DISCORDBOTSECRET")
client.run(token)
