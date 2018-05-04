import discord
import read_ramen
import os

token = os.getenv("BOT_TOKEN")
ramens = read_ramen.read_ramen()

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as {0} {1}".format(client.user.name, client.user.id))

@client.event
async def on_message(message):
    
    if message.content in ramens:
        if client.user != message.author:
            m = "https://twitter.com/sakamotogeki"
            await client.send_message(message.channel, m)

client.run(token)
