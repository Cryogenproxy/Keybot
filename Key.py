import discord
import os 
from discord.ext import commands
import asyncio

TOKEN = os.environ['TOKEN']
client = discord.Client()
client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print('bot is online')

@client.command()
async def ping(ctx):
    await ctx.send("pong You been Hacked Bitch")

@client.command()
async def skynet():
    await client.send_message(message.channel, 'Execute Y/N?')

@asyncio.coroutine
async def delete_messages(messages):
    if message.content == 'Y':
        await client.delete_messages()

client.run(TOKEN)
