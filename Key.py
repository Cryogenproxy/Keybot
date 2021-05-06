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

@client.event
async def on_disconnect():
    annoucment_channel = client.get_channel(697670402863792138)
    await annoucment_channel.send("Discord Bot Update, In Progress I will be Offline for a bit.")

@client.command
async def joined(ctx, *, member: discord.Member):
    await ctx.send('Welcome to the Server please read our #rules, and if you have any questions contact, a Moderator. We Welcome you to our Collective of Anonymous.')
    await ctx.send('{0} joined on {0.joined_at}'.format(member))
    
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

keep_alive()
client.run(TOKEN)
