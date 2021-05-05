import discord
import os 
import asyncio

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

@client.event

async def on_message(message):
    if message.content == 'skynet':
        await message.channel.send('Execute Y/N?')

@asyncio.coroutine
async def delete_messages(messages):
    if message.content == 'Y':
        await client.delete_messages()
        
client.run(TOKEN)
