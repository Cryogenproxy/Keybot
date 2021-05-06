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
@bot.command(pass_context=True)
@commands.has_role("Moderation")
async def Mute(ctx, user: discord.Member):
    role = discord.utils.find(lambda r: r.name == 'Member', ctx.message.guild.roles)
    if role in user.roles:
        await bot.say("{} is Muted".format(user))
    else:
        await bot.add_roles(user, role)

@client.command()
@bot.command(pass_context=True)
@commands.has_role("Moderation")
async def unmute(ctx, user: discord.Member):
    role = discord.utils.find(lambda r: r.name == 'Member', ctx.message.guild.roles)
    if role in user.roles:
        await bot.say("{} is not muted".format(user))
    else:
        await bot.add_roles(user, role)


keep_alive()
client.run(TOKEN)
