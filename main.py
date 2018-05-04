import discord
import ramen
import os

token = os.getenv("BOT_TOKEN")
ramens = ramen.read_ramens()

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as {0} {1}".format(client.user.name, client.user.id))

@client.event
async def on_message(message):
    if message.content in ramens.name.tolist():
        if client.user != message.author:
            m = ramens[ramens["name"] == message.content].twitter_url.values[0]
            await client.send_message(message.channel, m)

client.run(token)
