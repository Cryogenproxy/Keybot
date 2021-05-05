import discord
import os 

TOKEN = os.environ['TOKEN']
client = discord.Client()

@client.event
async def on_ready():
    print('bot is online')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$ping'):
        await message.channel.send('Pong Bitch you been hacked!')
client.run(TOKEN)
