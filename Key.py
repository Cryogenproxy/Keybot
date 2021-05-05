import discord
import os 
from discord.ext import commands


TOKEN = os.environ['TOKEN']
client = discord.Client()
client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print('bot is online')

@client.command()
async def ping(ctx):
    await ctx.send("pong You been Hacked Bitch")
client.run(TOKEN)
