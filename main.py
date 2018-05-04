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
    sentences = message.content.split()

    # 店舗名のみのメッセージ
    if client.user != message.author:
        if sentences[0] in ramens.name.tolist():
            m = ramens[ramens["name"] == sentences[0]].twitter_url.values[0]
            await client.send_message(message.channel, m)

        elif sentences[0] == "list"
            m = ramens.list_ramens()
            await client.send_message(message.channel, m)

client.run(token)
