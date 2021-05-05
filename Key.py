import discord
import os 
from discord.ext import commands
import webserver
from webserver import keep_alive
import asyncio

TOKEN = os.environ['TOKEN']
client = discord.Client()
client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print('bot is online')

@client.command()
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send("pong You been Hacked Bitch")

@client.command()
async def Help(ctx):
    await ctx.message.delete()
    await ctx.send("""
    
    $-help bring up help Menu 
    $-Ping for Testing Bot Response
    $-Purge Deletes groups of Messages
    """)

@client.command()
async def Purge(ctx):
    value = 10
    await ctx.message.delete(value)

keep_alive()
client.run(TOKEN)
